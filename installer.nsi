; Example NSIS script

; Name of the installer
OutFile "HRMSProjectInstaller.exe"

; Name of the application
Name "HRMSProject"

; Default installation directory
InstallDir "$PROGRAMFILES\\HRMSProject"

; Request application privileges for Windows Vista and above
RequestExecutionLevel admin

; Include the license agreement
LicenseText "Please read the following license agreement."
LicenseData "${__FILE__}\..\LICENSE.txt"

; Pages to display
Page license
Page directory
Page instfiles
UninstPage uninstConfirm
UninstPage instfiles

; Sections
Section "Install"
    ; Set output path to the installation directory
    SetOutPath "$INSTDIR"

    ; Copy files to the installation directory
    File /r "${__FILE__}\..\build\Release\*"

    ; Create a shortcut in the start menu
    CreateShortcut "$SMPROGRAMS\\HRMSProject.lnk" "$INSTDIR\\HRMSProject.exe"

    ; Create a shortcut on the desktop
    CreateShortcut "$DESKTOP\\HRMSProject.lnk" "$INSTDIR\\HRMSProject.exe"

    ; Write the uninstaller executable
    WriteUninstaller "$INSTDIR\\uninstall.exe"
SectionEnd

; Uninstaller
Section "Uninstall"
    ; Remove files
    Delete "$INSTDIR\\HRMSProject.exe"
    Delete "$INSTDIR\\*.*"

    ; Remove shortcuts
    Delete "$SMPROGRAMS\\HRMSProject.lnk"
    Delete "$DESKTOP\\HRMSProject.lnk"

    ; Remove directories
    RMDir "$INSTDIR"
SectionEnd

