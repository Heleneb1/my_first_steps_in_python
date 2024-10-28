def add_time(start, duration, start_day=None):
    # Cas spécial pour duration = "0:00"
    if duration == "0:00":
        if start_day:
            return f"{start}, {start_day.capitalize()}"
        return start

    # Séparation du temps de début et de la période (AM/PM)
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Conversion en minutes totales pour le temps de début
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Calcul du temps total en minutes
    total_minutes = (start_hour * 60 + start_minute + 
                     duration_hour * 60 + duration_minute)

    # Calcul des nouveaux jours, heures et minutes
    days_later = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)
    hours = remaining_minutes // 60
    minutes = remaining_minutes % 60

    # Détermination de la période (AM/PM)
    if hours == 0:
        period = "AM"
        hours = 12
    elif hours == 12:
        period = "PM"
        hours = 12
    elif hours > 12:
        period = "PM"
        hours -= 12
    else:
        period = "AM"

    # Construction du résultat
    new_time = f"{hours}:{minutes:02d} {period}"

    # Ajout du jour de la semaine si fourni
    if start_day:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        start_index = days.index(start_day.lower())
        new_day = days[(start_index + days_later) % 7].capitalize()
        new_time += f", {new_day}"

    # Ajout de l'indication des jours
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

print(add_time('3:30 PM', '2:12'))        # '5:42 PM'
print(add_time('11:55 AM', '3:12'))       # '3:07 PM'
print(add_time('2:59 AM', '24:00'))       # '2:59 AM (next day)'
print(add_time('11:59 PM', '24:05'))      # '12:04 AM (2 days later)'
print(add_time('8:16 PM', '466:02'))      # '6:18 AM (20 days later)'
print(add_time('11:40 AM', '0:00'))       # '11:40 AM'