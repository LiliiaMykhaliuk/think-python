'''
Exercises of the book "Think python"
16.7.1 Exercise:
'''

# Write a function called mul_time that takes a Time object and a number and
# returns a new Time object that contains the product of the original Time
# and the number.
# 
# Then use mul_time to write a function that takes a Time object that represents
# the finishing time in a race, and a number that represents the distance, and
# returns a Time object that represents the average pace (time per mile).


class Time:
    """Represents the time of the day

    attributes: hour, minute, second
    """

    def __init__(self, hour, minute, second):

        self.hour = hour
        self.minute = minute
        self.second = second

        # Convert time attributes if they are not valid
        self.make_time_valid()


    def __str__(self):
        """Prints the instance of the class in the right format"""

        return f"{self.hour} hours, {self.minute} minutes, {self.second} seconds"


    def make_time_valid(self):
        """Makes time valid if it's needed """

        if self.minute >= 60:
            additional_hours, valid_minutes = divmod(self.minute, 60)
            self.hour = self.hour + additional_hours
            self.minute = valid_minutes

        if self.second >= 60:
            additional_minutes, valid_seconds = divmod(self.minute, 60)
            self.minute = self.minute + additional_minutes
            self.second = valid_seconds


    def convert_time_into_seconds(self):
        """Converts time into seconds"""

        seconds = (self.hour * 3600) + (self.minute * 60) + self.second
        return seconds




def convert_seconds_into_time(seconds):
    """Converts seconds into time"""

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    time = Time(hours, minutes, seconds)
    return time



def mul_time(time_obj, number):
    """Creates a new Time object that contains the product of the original Time and the number"""

    # Multiply time in seconds by given number
    multiplied_amount_of_seconds = time_obj.convert_time_into_seconds() * number

    # Create new instance of Time class with new time
    new_time_obj = convert_seconds_into_time(multiplied_amount_of_seconds)
    return new_time_obj


def average_pace(time_obj, distance):
    """Calculate average time per mile"""

    # Get seconds per mile
    seconds_per_mile = time_obj.convert_time_into_seconds() / distance

    # Create new Time object with time per mile of a player
    time_per_mile = convert_seconds_into_time(seconds_per_mile)
    return time_per_mile


if __name__ == "__main__":

    # Set meeting time
    meeting_time = Time(9, 70, 0)

    # Reschedule meeting time by multiplying it with 2
    new_meeting_time = mul_time(meeting_time, 2)
    print(new_meeting_time)


    # Set parameters of a player in race
    finishing_time = Time(1, 13, 45)
    race_distance = 30

    # Get time per mile for the player
    player_average_pace = average_pace(finishing_time, race_distance)
    print(player_average_pace)
