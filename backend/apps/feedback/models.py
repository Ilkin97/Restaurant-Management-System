from django.db import models


class Feedback(models.Model):
    """
    A model representing customer feedback.

    This model stores information about feedback submitted by users,
    including their name, email, message, rating, and the date of submission.
    """

    name = models.CharField(max_length=100)
    """
    The name of the person submitting the feedback.
    The maximum length of the name is 100 characters.
    """

    email = models.EmailField()
    """
    The email address of the person submitting the feedback.
    This field will store the email in a valid format.
    """

    message = models.TextField()
    """
    The content of the feedback message provided by the user.
    This is a text field to accommodate longer messages.
    """

    rating = models.PositiveSmallIntegerField(choices=[
        (1, '1 - Very Bad'),
        (2, '2 - Bad'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ])
    """
    The rating given by the user, which is a small positive integer.
    The choices are from 1 (Very Bad) to 5 (Excellent).
    """

    created_at = models.DateTimeField(auto_now_add=True)
    """
    The timestamp when the feedback was created. This field is automatically 
    set to the current time when the feedback is created.
    """

    def __str__(self):
        """
        String representation of the Feedback instance.

        Returns:
            str: A formatted string representing the feedback with the 
                 submitter's name and rating (e.g., "John Doe (4/5)").
        """
        return f"{self.name} ({self.rating}/5)"
