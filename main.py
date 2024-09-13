import discord
from datetime import datetime, time, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone as pytimezone
import asyncio
import random
import holidays

TOKEN = 'MTI3Mjc0MzY3OTg4NjYyMjgzMQ.Gxm3dc.j2DgeauElAmJ104FXdWXIkoR7Sb8fGVKq93AQo'
CHANNEL_ID = 1272594921601237042  # Replace with your channel ID
ROLE_ID = 1206860573375987762 

# Set up the client
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
client = discord.Client(intents=intents)

# Define the EST timezone
est = pytimezone('America/New_York')

# Define time bounds in EST
start_time = time(9, 30)
end_time = time(16, 0)


# Sample messages:
messages = [
    "Align your decisions with your values—start the 4-Step Process now.",
    "Focus on what matters most. Are you practicing the 4-Steps today?",
    "Remember why you started. Take a moment for the 4-Step Sound Psych Process.",
    "Your values are your compass—use the 4-Steps to navigate your day.",
    "Strengthen your focus, reinforce your values—time for the 4-Steps.",
    "Honor your commitments to yourself—do the 4-Steps now.",
    "One step closer to balance—take time for the 4-Step Process.",
    "Have you checked in with your values today? Do the 4-Steps.",
    "A small effort now leads to big gains later—work the 4-Steps.",
    "Let your actions reflect your priorities—engage in the 4-Step Process.",
    "Your future self will thank you—start the 4 Steps today.",
    "Remember, consistency builds mastery—do the 4-Steps.",
    "Stay true to your values—commit to the 4-Step Process.",
    "Your best decisions come from a clear mind—take time for the 4-Steps.",
    "Keep your goals in sight—use the 4-Steps to stay on track.",
    "Success is built on small, consistent actions—do the 4-Steps.",
    "Your values guide your path—let the 4 steps lead the way.",
    "Pause, reflect, and act—time for the 4-Step Process.",
    "Let your actions today reflect the person you want to become—start with the 4 steps.",
    "Balance your life, balance your trading—practice the 4-Steps.",
    "Are your decisions aligning with your values? Take a moment for the 4-Steps.",
    "Prioritize what matters—use the 4-Steps to guide your day.",
    "Small steps, big impact—work through the 4 Steps.",
    "Focus on your values, focus on the 4-Step Process.",
    "The best decisions are value-driven—take time for the 4-Steps.",
    "Remember your why—start with the 4-Step Sound Psych Process.",
    "Consistency breeds success—commit to the 4-Steps.",
    "Align your actions with your aspirations—do the 4 steps.",
    "Stay grounded in your values—practice the 4-Steps.",
    "Your values are the foundation of your decisions—use the 4-Steps.",
    "Strength comes from within—nurture it with the 4-Step Process.",
    "Stay focused, stay committed—start the 4-Steps today.",
    "Your values deserve your attention—take time for the 4-Steps.",
    "The 4-Steps are your pathway to clarity—use them wisely.",
    "Prioritize your well-being—engage in the 4-Step Process.",
    "Let today’s decisions reflect your deepest values—start with the 4-Steps.",
    "Mindful actions lead to meaningful outcomes—practice the 4-Steps.",
    "Your success is rooted in your values—do the 4-Steps.",
    "Ground yourself in what matters most—begin the 4-Step Process.",
    "Align your life with your values—use the 4 Steps as your guide.",
    "Your values are the bedrock of your decisions—commit to the 4-Steps.",
    "Clear your mind, focus your energy—take time for the 4-Steps.",
    "Let your decisions today reflect your values—start the 4-Steps.",
    "Stay true to your path—use the 4 steps to stay aligned.",
    "Your values are your anchor—practice the 4-Step Process.",
    "Consistency is key—commit to the 4-Steps today.",
    "Stay focused on what matters—take time for the 4-Step Sound Psych Process.",
    "Let your values guide your actions—start with the 4 steps.",
    "Reinforce your values with mindful decisions—practice the 4-Steps.",
    "Align your trading with your life’s values—take time for the 4-Steps.",
    "Keep your priorities straight—do the 4-Steps now.",
    "The 4-Steps are your roadmap to balanced decisions—use them.",
    "Stay grounded in your values—take a moment for the 4-Step Process.",
    "Reflect, realign, and act—engage in the 4-Steps.",
    "Your decisions shape your future—make them count with the 4-Steps.",
    "Stay true to your values—commit to the 4-Step Sound Psych Process.",
    "Consistency builds resilience—practice the 4-Steps today.",
    "Your best decisions come from a calm mind—use the 4-Steps.",
    "Keep your values front and center—start the 4-Steps now.",
    "Small actions lead to big changes—commit to the 4-Steps.",
    "Stay aligned with your values—practice the 4-Step Process.",
    "Remember what matters—take time for the 4-Steps.",
    "Your values are your guide—use the 4-Steps to stay on course.",
    "Stay focused, stay aligned—commit to the 4-Steps.",
    "Let your values guide your actions—practice the 4-Step Process.",
    "Your decisions reflect your priorities—make them count with the 4-Steps.",
    "Reinforce your values with every decision—use the 4-Steps.",
    "Stay true to your path—practice the 4 Steps today.",
    "Let your deepest values guide your actions today—start with the 4 steps.",
    "Your values are your compass—use the 4-Steps to navigate your day.",
    "Stay committed to your values—do the 4-Steps now.",
    "Consistency leads to mastery—practice the 4-Steps.",
    "Let your values drive your decisions—take time for the 4-Step Process.",
    "Small steps, big impact—engage in the 4-Steps.",
    "Stay aligned with your values—use the 4 Steps as your guide.",
    "Your decisions today shape your tomorrow—commit to the 4-Steps.",
    "Stay focused on your values—take time for the 4-Step Sound Psych Process.",
    "Your values are your foundation—practice the 4-Steps now.",
    "Stay true to your principles—use the 4-Steps to stay grounded.",
    "Your best decisions come from a clear mind—engage in the 4-Step Process.",
    "Let your actions reflect your priorities—commit to the 4-Steps.",
    "Stay focused on what matters most—practice the 4-Steps today.",
    "Your values deserve your attention—take time for the 4-Step Process.",
    "Small, consistent actions lead to big results—commit to the 4-Steps.",
    "Your values are your anchor—stay grounded with the 4-Steps.",
    "Let your decisions reflect your deepest values today—start the 4-Step Process.",
    "Stay true to your values—commit to the 4-Steps now.",
    "Your actions today shape your future—make them count with the 4-Steps.",
    "Stay aligned with your values—practice the 4-Step Sound Psych Process.",
    "Your best decisions come from a place of clarity—use the 4-Steps.",
    "Let your values guide your path—commit to the 4-Steps.",
    "Stay focused, stay true—practice the 4-Step Process today.",
    "Your values are your compass—use the 4-Steps to stay on course.",
    "Consistency builds success—engage in the 4-Steps now.",
    "Let your decisions reflect your principles—commit to the 4-Steps.",
    "Stay aligned with your values—take time for the 4-Step Process.",
    "Your actions today reflect your priorities—make them count with the 4-Steps.",
    "Let your values guide your decisions—practice the 4-Step Sound Psych Process.",
    "Stay true to your path—commit to the 4 steps now.",
    "Your future self will thank you—take time for the 4-Step Process today.",
]


# US holidays
us_holidays = holidays.US(years=datetime.now().year, observed=True)

async def send_message():
    now = datetime.now(est).time()
    print(f'Message sending now ----->')
    if start_time <= now <= end_time:
        channel = client.get_channel(CHANNEL_ID)
        if channel:
            role = discord.utils.get(channel.guild.roles, id=ROLE_ID)
            if role:
                selected_message = random.choice(messages)
                message_content = f"{role.mention} {selected_message}"
                
                message = await channel.send(
                    message_content, 
                    allowed_mentions=discord.AllowedMentions(roles=True)
                )
                print(f'Message sent at {datetime.now(est)}')

                await asyncio.sleep(15 * 60)  # Wait for 15 minutes
                await message.delete()
                print(f'Message deleted after 15 minutes at {datetime.now(est)}')

async def schedule_daily_messages(scheduler):
    scheduler.remove_all_jobs()  # Remove previous day's jobs if any

    today = datetime.now(est).date()
    if today in us_holidays or today.weekday() >= 5:
        print('Today is a holiday or weekend. No messages will be scheduled.')
        return

    start_dt = est.localize(datetime.combine(today, start_time))
    end_dt = est.localize(datetime.combine(today, end_time))

    min_interval_seconds = 40 * 60  # 40 minutes in seconds
    total_seconds = int((end_dt - start_dt).total_seconds())
    
    if total_seconds < min_interval_seconds * 5:
        print('Not enough time in the day to schedule 5 messages with at least 40 minutes between them.')
        return

    # Determine the exact times for the messages
    timestamps = []
    current_time = start_dt
    for _ in range(5):
        random_offset = random.randint(0, min_interval_seconds - 1)
        current_time += timedelta(seconds=min_interval_seconds + random_offset)
        timestamps.append(current_time)

    # Schedule the messages
    for timestamp in timestamps:
        scheduler.add_job(send_message, 'date', run_date=timestamp)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    scheduler = AsyncIOScheduler()
    
    # Schedule the task to set up the daily message schedule at 9:25 AM EST every day
    scheduler.add_job(schedule_daily_messages, 'cron', hour=9, minute=25, timezone=est, args=[scheduler])
    
    # Initial call to set up today's schedule
    await schedule_daily_messages(scheduler)

    scheduler.start()

client.run(TOKEN)
