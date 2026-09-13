# Camera Experiences

Use this reference for capture apps that must choose among Duo's front cameras, respond to display-relative camera direction, compose previews, or show supplementary UI on both displays.

All new iOS 27.1 names below are transcript-derived and **Documentation pending**. See `api-status.md` before producing code.

## Choose the camera strategy

| Requirement | Prefer | Tradeoff stated by Apple |
|---|---|---|
| Seamless inner/outer front-camera switching with common capture features | Virtual Front Camera | Automatically selects the relevant physical front camera; capability limited to the intersection of both cameras |
| Higher resolution/frame rate on the outer front camera | Individual physical camera | App must coordinate switching as the device/display relationship changes |
| Depth capture | Individual physical camera | Apple says depth is available only when accessing individual cameras |
| One capture UI that can face different physical directions | Individual cameras plus direction coordinator | More control and more responsibility |

Apple describes discovery of the Virtual Front Camera through `AVCaptureDeviceDiscoverySession` using `.front` position with wide or ultrawide device type. The exact virtual device-type constant is not shown; do not invent it. [TT-111465]

### Capability statements from the talk

- Inner ultrawide front camera: up to 1080p video at 60 fps.
- Outer ultrawide front camera: up to 4K video at 120 fps.
- Virtual Front Camera: shared capabilities, stated maximum 1080p at 60 fps.
- Depth: individual physical-camera access only. [TT-111465]

Treat these as talk evidence, not a replacement for runtime format discovery. Production code should still choose supported formats from the selected `AVCaptureDevice` rather than hard-code one assumed format.

## Position is not direction

Both physical front cameras report `AVCaptureDevice.position == .front`, but a camera may face toward or away from the person depending on which display contains the app view and how the open device is oriented. Rear cameras can also become forward-facing relative to a view shown on the outer display. [TT-111465]

Use fixed device position for the hardware category. Use the direction coordinator for facing relative to a particular app view.

## Direction-coordinator architecture

Create one coordinator per relevant `UIView`, with the device types the feature may use. Each coordinator's result is relative to its own view. Two simultaneous display views therefore require two coordinators. [TT-111465]

Transcript-shown setup:

```swift
directionCoordinator = AVCaptureDeviceDirectionCoordinator(
    view: view,
    deviceTypes: [
        .builtInOuterUltraWideCamera,
        .builtInInnerUltraWideCamera,
        .builtInDualWideCamera,
    ],
    changeHandler: { [weak self] map in
        self?.updateCameraSession(map)
    }
)
```

The talk states that the coordinator is in AVKit and is main-actor isolated because it is tied to a view. It provides `AVCaptureDeviceDescriptor` values rather than passing `AVCaptureDevice` directly; Apple describes the descriptor as main-actor-safe and sendable for transfer to a camera actor. [TT-111465]

Do not infer the map type, descriptor-to-device construction call, lifetime method, cancellation behavior, or session threading beyond those statements.

### Change-handler responsibilities

When direction changes: [TT-111465]

1. Select the camera that should now be forward-facing for the current view.
2. Pass descriptor-level information across the appropriate isolation boundary.
3. Reconfigure `AVCaptureSession` in the camera-owned execution context; do not call AVFoundation session APIs directly inside the view-bound change handler.
4. Re-evaluate preview mirroring. Apple specifically recommends mirroring when a rear camera becomes forward-facing for a natural selfie experience.
5. Coordinate any user-interface update with the camera transition.

Preserve capture intent and controls throughout reconfiguration. A direction change should not silently reset mode, stop an in-progress user task without handling it, or expose stale camera labels.

## Dual-display capture

Camera apps can show views on both displays using scene accessories. Direction remains per view: the same physical camera can be forward-facing relative to one view and backward-facing relative to another. [TT-111464, TT-111465]

For `CameraCaptureAccessory` lifecycle and availability, read `displays-scenes-and-hinge.md`. Register supplementary UI on the camera feature view and disable its toggle when the system reports the accessory unavailable.

## Preview composition

The inner display may leave unused space around a rear-camera preview. Apple presents two valid designs: offset the preview and use remaining space for controls, or fill the display. Choose according to content/capture needs, then keep controls safe and reachable. [TT-111465]

Use the established `AVCaptureVideoPreviewLayer.videoGravity` property to choose how video occupies layer bounds. Do not infer a Duo-specific gravity mode.

Apple recommends using the square front sensors with `dynamicAspectRatio` to choose a landscape aspect ratio on the inner display: [TT-111465]

```swift
class AVCaptureDevice {
    // ...
    var dynamicAspectRatio: AVCaptureDevice.AspectRatio? { get }
}
```

This is the declaration shape shown in the talk, not sufficient evidence for how to select or apply a ratio. Keep implementation details pending.

### Camera occlusion

If the viewfinder is central to the experience, keep essential content and controls clear of the active inner camera region. Query occlusion reserved regions for custom placement rather than assuming a camera frame. [TT-111463]

## Rotation

Apple recommends adopting the camera rotation coordinator so preview and captured media remain upright when a scene moves between displays. The transcript does not name or show the coordinator's exact declaration. [TT-111465]

After adopting it, Apple says to disable camera-sensor-orientation compensation for improved performance; the shown property shape is:

```swift
class AVCapturePhotoOutput: AVCaptureOutput {
    // ...
    var isCameraSensorOrientationCompensationEnabled: Bool { get set }
}
```

Apple states this compensation is enabled on all Duo front cameras. Do not disable it until the actual rotation-coordinator integration has been validated. Exact availability and interactions remain documentation pending. [TT-111465]

## Failure and transition cases

Design for:

- Selected physical camera becoming inappropriate as the device opens/closes
- A scene moving between displays while capture is configured
- Different direction results from two simultaneous view coordinators
- Accessory becoming unavailable while user-enabled state remains true
- Session reconfiguration delay or failure
- Preview mirroring changing with direction
- Aspect-ratio change without stretching or hiding essential content
- Rotation during or immediately after display movement

The talks do not specify a failure API. Use the existing app's AVFoundation error model and avoid claiming a Duo-specific recovery callback.

## Review checklist

- [ ] Virtual versus individual camera chosen from required capability, not device detection
- [ ] Physical formats discovered at runtime; talk maxima not hard-coded as universal availability
- [ ] `position` not mistaken for direction relative to the current view
- [ ] One direction coordinator per simultaneous display view
- [ ] View-bound callback avoids direct capture-session operations
- [ ] Descriptor handoff and camera-session isolation follow only documented/talk-stated guarantees
- [ ] Camera reconfiguration, mirroring, UI labels, and capture state transition coherently
- [ ] Preview fill/offset choice preserves safe, reachable controls
- [ ] Camera occlusion handled with reserved-region data, not fixed coordinates
- [ ] Rotation behavior tested across display changes before disabling compensation
- [ ] Accessory availability and user preference modeled separately

## Related references

- Multi-display accessories and scene state: `displays-scenes-and-hinge.md`
- Camera occlusion and custom placement: `reserved-regions-and-arrangements.md`
- Camera validation matrix: `testing-and-validation.md`
