class InvalidVersion(Exception):
    """Exception raised for invalid version strings."""
    pass

class Version:
    """Class representing a version."""
    def __init__(self, version: str):
            if not self._is_valid_version(version):
                raise InvalidVersion(f"Invalid version string: {version}")
            self.version = version
    
    def _is_valid_version(self, version: str) -> bool:
        # Add your version validation logic here
        import re
        pattern = r'^\d+\.\d+\.\d+$'  # Example pattern for semantic versioning
        if not re.match(pattern, version):
            return False
        
        parts = version.split('.')
        if len(parts) != 3 or not all(part.isdigit() for part in parts):
            raise InvalidVersion("Version must be in the format 'X.Y.Z' where X, Y, and Z are integers.")
        
        self.major, self.minor, self.patch = map(int, parts)
        return True

    def __str__(self):
        return self.version