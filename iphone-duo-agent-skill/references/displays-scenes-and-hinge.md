# Displays, Scenes, and Hinge Input

Use view- and scene-local state. iPhone Duo can resize one scene, run two apps side by side, support multiple instances of an app's UI, or pair a main scene with supplementary content on another display. [TT-111461, TT-111464]

All new iOS 27.1 names below are transcript-derived and **Documentation pending**. See `api-status.md`.

## Separate the inputs

Do not collapse these concepts into one `isDuoOpen` flag:

| Input | Use it for |
|---|---|
| Horizontal/vertical size classes | Broad compact-versus-regular experience |
| View/container geometry | Continuous layout and local aspect ratio |
| Scene geometry / scene-local screen | Display-local decisions when truly necessary |
| Reserved regions | Custom avoidance/displacement around a fold or camera |
| Hinge status/angle | Live interaction or visual effect tied to physical motion |
| Scene/accessory availability | Enabling controls that request extra UI or another display |

Each input answers a different question. Hinge state does not tell an agent the available frame, size class, scene count, accessory availability, or camera direction.

## Display-local reasoning

- Avoid global screen state and `UIScreen.main`; resolve a screen dynamically from the owning `UIWindowScene` only if local geometry is insufficient. [TT-111461]
- When two app views are visible on different displays, compute direction, layout, and accessory state relative to each view/scene. [TT-111464, TT-111465]
- Do not name an inner scene `main` and an outer scene `secondary` in domain logic. The user's active task and system availability determine roles.
- Keep shared task/domain state separate from display-specific presentation state. This enables continuity without forcing both scenes to share transient geometry.

## Multitasking and multiple scenes

Apple says all apps participate in Duo side-by-side multitasking, and video-plus-app layouts present as dynamic resizing from the app's perspective. Use size classes and scene geometry rather than special-casing each composition. [TT-111464]

iPhone Duo is described as the first iPhone that can support multiple instances of an app's UI. Apps that already support this on iPad inherit relevant behavior, but scene creation availability differs: Apple states new windows cannot be created on the outer display and can be created on the inner display. [TT-111464]

Operational rules:

1. Treat new-scene creation as dynamically available.
2. Surface or hide creation affordances through system behavior when possible.
3. Handle scene activation request errors; never assume a request succeeds because multiwindow support exists.
4. Store navigation/draft state at the correct scene or document scope so one instance does not overwrite another.

The talk names `UIWindowSceneActivationAction` as automatically hiding when new windows are unavailable, but shows no declaration. Do not fabricate construction or error-handling syntax. [TT-111464]

## Hinge observation

Apple names three high-level statuses—closed, partially open, fully open—and states that SwiftUI `onHingeChange` and UIKit `UIHingeInteraction` also provide continuous angle updates. [TT-111464]

### Appropriate uses

- Animate an effect that should track physical opening/closing.
- Drive an interaction analogous to the talk's pitch-bend/whammy example.
- Update nonessential visual response while maintaining equivalent controls without hinge data.

### Inappropriate uses

- Reconstruct safe areas or reserved-region frames from angle.
- Choose primary layout breakpoints that size classes, geometry, or arrangements should own.
- Require a hinge for core functionality.
- Invent degree thresholds for Apple's status values.

### Transcript pattern

```swift
struct InstrumentView: View {
    @State private var pitchBend: Double = 0

    var body: some View {
        GuitarView(pitchBend: pitchBend)
            .onHingeChange { _, context in
                if let hinge = context.hinge,
                   hinge.status == .partiallyOpen {
                    pitchBend = calculatePitchBend(angle: hinge.angle)
                } else {
                    pitchBend = 0
                }
            }
    }

    private func calculatePitchBend(angle: Angle) -> Double {
        // Product mapping; the talk omits its implementation.
        // ...
    }
}
```

This preserves two critical rules from the talk: hinge can be absent on a device without one, and the effect resets when the relevant hinge state ends. The transcript does not define the context types, delivery guarantees, or angle mapping. [TT-111464]

For UIKit, the talk names `UIHingeInteraction` but provides no usage. Do not invent a delegate, closure, initializer, or callback signature.

## Scene accessories

Scene accessories pair supplementary content with a main UI and can use another display. The system controls availability dynamically; accessories are enabled by default but can be toggled. Apps must observe availability changes so controls remain synchronized. [TT-111464]

### Camera capture accessory

Apple introduces `CameraCaptureAccessory` for showing camera-related supplementary UI on the outer display while the main camera UI remains on the inner display. The talk states it is available when the app is full-screen on the inner display with an active camera session. Register it on the view whose lifetime should own the accessory. [TT-111464]

Transcript-shown SwiftUI pattern:

```swift
struct CameraRootView: View {
    @State private var model = TeleprompterModel()

    var body: some View {
        CameraView(model: model)
            .sceneAccessory {
                CameraCaptureAccessory(isEnabled: $model.isEnabled) {
                    TeleprompterView(model: model)
                }
                .onAvailabilityChange { newValue in
                    model.isAvailable = newValue
                }
            }
            .toolbar {
                TeleprompterToggle(isEnabled: $model.isEnabled)
                    .disabled(!model.isAvailable)
            }
    }
}
```

Operational implications:

- Scope registration to the camera view so accessory lifetime follows feature visibility.
- Store user-enabled and system-available as separate states.
- Disable the toggle when unavailable; do not imply that user preference can override system availability.
- Share only the domain state needed by both representations. Keep scene-local layout/focus separate.

The talk does not establish the complete accessory type hierarchy, concurrency model, callback delivery, or UIKit equivalent.

## Continuity architecture

Use three state layers:

1. **Task/domain state:** selection, draft, playback/capture intent; should survive resize and display movement.
2. **Scene state:** navigation path, presented detail, per-window focus; owned by each scene unless product semantics require sharing.
3. **Presentation state:** measured geometry, arrangement placement, bar axis, active regions; recomputed from the current view/scene.

This is an implementation heuristic derived from Apple's requirement that opening/closing remain one predictable experience; it is not a new Duo API contract. [TT-111466]

## Review checklist

- [ ] No global screen singleton or display role baked into domain state
- [ ] Layout, hinge, region, and accessory availability modeled as distinct inputs
- [ ] Scene creation affordance/error handling accounts for dynamic availability
- [ ] Hinge behavior remains optional and resets when hinge/context is absent or inapplicable
- [ ] Hinge angle not used to recreate primary layout
- [ ] Accessory is scoped to the owning feature view
- [ ] Accessory enablement and availability modeled independently
- [ ] Shared state excludes per-display geometry and focus unless intentionally synchronized
- [ ] Open/close or scene movement preserves active user task

## Related references

- Reserved regions and arrangements: `reserved-regions-and-arrangements.md`
- Camera direction per display: `camera-experiences.md`
- Continuity and accessibility: `continuity-and-accessibility.md`
- Configuration tests: `testing-and-validation.md`
