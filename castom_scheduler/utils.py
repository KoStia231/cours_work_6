from apscheduler.triggers.cron import CronTrigger

from mail.models import Mailing


def get_mailing_period_trigger(mailing: Mailing) -> CronTrigger:
    start_date = mailing.start_date

    if mailing.period == Mailing.Period.CUSTOM:
        trigger = CronTrigger(second='*/5', start_date=start_date)
    elif mailing.period == Mailing.Period.DAILY:
        trigger = CronTrigger(
            day='*', hour=start_date.hour, minute=start_date.minute, start_date=start_date
        )
    elif mailing.period == Mailing.Period.WEEKLY:
        trigger = CronTrigger(
            day_of_week=start_date.weekday(),
            hour=start_date.hour,
            minute=start_date.minute,
            start_date=start_date,
        )
    elif mailing.period == Mailing.Period.MONTHLY:
        trigger = CronTrigger(
            month='*',
            day=start_date.day,
            hour=start_date.hour,
            minute=start_date.minute,
            start_date=start_date,
        )
    else:
        raise NotImplementedError

    return trigger



