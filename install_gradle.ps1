# PowerShell script to download and install Gradle on Windows

# Set the version of Gradle you want to install
$gradleVersion = "8.4.1"
$gradleZipUrl = "https://services.gradle.org/distributions/gradle-$gradleVersion-bin.zip"
$gradleInstallDir = "C:\Gradle"

# Create the installation directory
New-Item -ItemType Directory -Force -Path $gradleInstallDir

# Download the Gradle ZIP file
$gradleZipPath = "$gradleInstallDir\gradle-$gradleVersion-bin.zip"
Invoke-WebRequest -Uri $gradleZipUrl -OutFile $gradleZipPath

# Extract the ZIP file
Expand-Archive -Path $gradleZipPath -DestinationPath $gradleInstallDir

# Set the PATH environment variable
$gradleBinPath = "$gradleInstallDir\gradle-$gradleVersion\bin"
[System.Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";$gradleBinPath", [System.EnvironmentVariableTarget]::Machine)

# Clean up the ZIP file
Remove-Item -Force $gradleZipPath

# Verify the installation
Write-Output "Gradle $gradleVersion installed successfully."
Write-Output "Restart your terminal or IDE to use the new PATH."