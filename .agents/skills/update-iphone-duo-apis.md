# Maintenance: iPhone Duo iOS 27.1 API Refresh

The executable maintenance skill is [`update-iphone-duo-apis/SKILL.md`](update-iphone-duo-apis/SKILL.md). Its scan manifest is [`update-iphone-duo-apis/references/scan-manifest.md`](update-iphone-duo-apis/references/scan-manifest.md).

Invoke it after Apple publishes or revises the iOS 27.1 iPhone Duo API documentation:

```text
Use $update-iphone-duo-apis to verify the pending iPhone Duo APIs and refresh the skill references.
```

The workflow requires network access to official Apple sources and a released iOS 27.1 SDK for compilation validation.
