from django.db import models


class Advertisement(models.Model):
    """
    A model to represent an advertisement in the system.

    The Advertisement model contains information about an advertisement such as:
    - Title: A brief title for the advertisement.
    - Description: A more detailed description of the advertisement.
    - Image: A field to store an image related to the advertisement.
    - Active Status: A boolean to indicate if the advertisement is currently active.
    - Created At: The timestamp when the advertisement was created.
    - Expires At: An optional timestamp indicating when the advertisement expires.
    """
    
    # The title of the advertisement (up to 200 characters)
    title = models.CharField(max_length=200)

    # The description of the advertisement (can be left blank)
    description = models.TextField(blank=True)

    # The image associated with the advertisement
    image = models.ImageField(upload_to='ads/')

    # Boolean field to mark if the advertisement is active or not
    is_active = models.BooleanField(default=True)

    # Timestamp for when the advertisement was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Optional expiry date for the advertisement
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """
        String representation of the Advertisement instance.

        Returns the title of the advertisement when printed.
        """
        return self.title
