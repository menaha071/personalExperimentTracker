from datetime import date
from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def send_reminder_email(to_email, experiment_name):
    """Send a reminder email for a specific experiment"""
    try:
        msg = Message(
            subject=f"⏰ Reminder: Log your '{experiment_name}' today!",
            sender=current_app.config['MAIL_USERNAME'],
            recipients=[to_email]
        )
        msg.body = f"""
Hi there!

Don't forget to log your experiment: {experiment_name} today.

Keep the streak going! 💪

- Personal Experiment Tracker
        """
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

def check_and_send_reminders(db, Experiment, User):
    """Check all active experiments and send reminders"""
    today = date.today()
    active_experiments = Experiment.query.filter_by(is_active=True).all()

    for experiment in active_experiments:
        already_logged = any(
            entry.date == today
            for entry in experiment.entries
        )
        if not already_logged:
            user = User.query.get(experiment.user_id)
            if user and user.email:
                send_reminder_email(user.email, experiment.name)
                print(f"Reminder sent to {user.email} for '{experiment.name}'")

def schedule_reminders(app, db, Experiment, User):
    """Set up APScheduler to run reminders daily at 8 AM"""
    try:
        from apscheduler.schedulers.background import BackgroundScheduler
        scheduler = BackgroundScheduler()
        scheduler.add_job(
            func=lambda: check_and_send_reminders(db, Experiment, User),
            trigger='cron',
            hour=8,
            minute=0,
            id='daily_reminder'
        )
        scheduler.start()
        print("✅ Reminder scheduler started.")
    except Exception as e:
        print(f"Scheduler error: {e}")
