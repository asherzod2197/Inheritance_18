# 18. Xona harorati

class Room:
    def __init__(self, room_type, temperatures):
        self.room_type = room_type          # "Yotoqxona", "Oshxona", "Zal" va h.k.
        self.temperatures = temperatures    # haroratlar ro'yxati (°C)

    def average_temperature(self):
        """O'rtacha harorat = haroratlar yig'indisi / soni"""
        if not self.temperatures:
            return 0.0
        return sum(self.temperatures) / len(self.temperatures)

    def __str__(self):
        avg = self.average_temperature()
        return f"{self.room_type:12} | Kuzatuvlar: {len(self.temperatures):2} | O‘rtacha: {avg:5.1f} °C"


# -----------------------------------------------
# Voris sinflar (emoji va chiroyli chiqish)
# -----------------------------------------------

class Bedroom(Room):
    def __str__(self):
        avg = self.average_temperature()
        comfort = "😴 qulay" if 20 <= avg <= 24 else "⚠️ noqulay"
        return f"🛏️  {self.room_type:10} → o‘rtacha {avg:4.1f} °C  ({comfort})"


class Kitchen(Room):
    def __str__(self):
        avg = self.average_temperature()
        comfort = "🍳 normal" if 19 <= avg <= 23 else "⚠️ ehtiyot bo‘ling"
        return f"🔥 {self.room_type:10} → o‘rtacha {avg:4.1f} °C  ({comfort})"


# --------------------------------------------------
# Harorat statistikasini chiqarish
# --------------------------------------------------

def show_temperature_summary(rooms):
    print("\n" + "═" * 60)
    print("     XONALAR HARORATI — O‘RTACHA KO‘RSATKICHLAR     ".center(60))
    print("═" * 60)
    print("Xona turi          | Kuzatuvlar | O‘rtacha harorat (°C)")
    print("─" * 60)

    total_temp_sum = 0
    total_measurements = 0

    for room in rooms:
        print(room)
        avg = room.average_temperature()
        count = len(room.temperatures)
        total_temp_sum += avg * count
        total_measurements += count

    if total_measurements > 0:
        house_avg = total_temp_sum / total_measurements
        print("─" * 60)
        print(f"Uy bo‘ylab umumiy o‘rtacha harorat:       {house_avg:5.1f} °C")
    print("═" * 60 + "\n")


# Test ma'lumotlari
xonalar = [
    Bedroom("Yotoqxona", [22.5, 23.0, 21.8, 22.7]),
    Kitchen("Oshxona", [21.0, 22.0, 23.5, 21.2]),
    Bedroom("Bolalar xonasi", [20.5, 21.0, 19.8]),
    Kitchen("Katta oshxona", [24.0, 23.8]),
]

show_temperature_summary(xonalar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol ma'lumotlaringiz:\n")
misol_xonalar = [
    Bedroom("Yotoqxona", [22.5, 23.0]),
    Kitchen("Oshxona", [21.0, 22.0]),
]

show_temperature_summary(misol_xonalar)
