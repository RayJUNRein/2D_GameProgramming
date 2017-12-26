; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{48470909-5EC0-4FCB-B9AF-4335D2A9634D}
AppName=MidnightWanderers_2013130042_Setup
AppVersion=1.5
;AppVerName=MidnightWanderers_2013130042_Setup 1.5
AppPublisher=DaEun_Han
AppPublisherURL=https://blog.naver.com/rayjun_ddubi
AppSupportURL=https://blog.naver.com/rayjun_ddubi
AppUpdatesURL=https://blog.naver.com/rayjun_ddubi
DefaultDirName={pf}\MidnightWanderers_2013130042_Setup
DisableProgramGroupPage=yes
OutputDir=C:\Users\zkalk\Desktop
OutputBaseFilename=MidnightWanderers_2013130042_Setup
SetupIconFile=D:\RayJUN_House\Study\2D_GameProgramming\Project\2DGP_Project_10th\MidnightWanderers\dist\Resources\MidnightWanderers_Icon.jpg
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\RayJUN_House\Study\2D_GameProgramming\Project\2DGP_Project_10th\MidnightWanderers\dist\MidnightWanderers.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\RayJUN_House\Study\2D_GameProgramming\Project\2DGP_Project_10th\MidnightWanderers\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\MidnightWanderers_2013130042_Setup"; Filename: "{app}\MidnightWanderers.exe"
Name: "{commondesktop}\MidnightWanderers_2013130042_Setup"; Filename: "{app}\MidnightWanderers.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\MidnightWanderers.exe"; Description: "{cm:LaunchProgram,MidnightWanderers_2013130042_Setup}"; Flags: nowait postinstall skipifsilent
