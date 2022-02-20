import pytest
import smtplib
from twilio.rest import Client
from src.notification_manager import NotificationManager

class TestNotificationManager:

    @pytest.fixture(scope='module')
    def notification_manager(self):
        try:
            self.notification_manager = NotificationManager()
        finally:
            pass
        return self.notification_manager

    def test_it_can_send_sms(self, notification_manager):
        try:
            status_message = notification_manager.send_message("test")
        except:
            assert False
        else:
            assert status_message

    def test_it_can_send_email(self, notification_manager):
        try:
            notification_manager.send_emails("kichichoi102@gmail.com", "test")
        except smtplib.SMTPConnectError:
            assert False
        else:
            assert True