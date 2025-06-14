import krpc
import time 
import csv

# Connect to kRPC server
conn = krpc.connect(name='kerbnik-1')
vessel = conn.space_center.active_vessel

# Reference frame
orbital_frame = vessel.orbit.body.reference_frame
flight = vessel.flight(orbital_frame)
resources = vessel.resources

# Get two 2HOT Thermometers (assumed: one inside, one outside)
thermometers = [part for part in vessel.parts.all if '2HOT' in part.title]
if len(thermometers) < 2:
    raise Exception("Need at least two 2HOT Thermometers (one inside, one outside)")

inside_thermometer = thermometers[0]
outside_thermometer = thermometers[1]

# Path to CSV output
path = "data\\telemetry\\kerbnik_1_telemetry.csv"

with open(path, "w", newline='') as f:
    writer = csv.writer(f)

    # CSV Header
    writer.writerow([
        'Time', 'Altitude (m)', 'Orbital Velocity (m/s)',
        'Apoapsis (m)', 'Periapsis (m)', 'Inclination (deg)',
        'Battery (%)', 'Inside Temp (K)', 'Outside Temp (K)'
    ])

    # Main logging loop
    while True:
        # Battery status
        electric_charge = resources.amount('ElectricCharge')
        electric_max = resources.max('ElectricCharge')
        battery_percent = (electric_charge / electric_max) * 100 if electric_max > 0 else 0

        if electric_charge <= 0.1:
            print("Battery depleted. Logging stopped.")
            break

        # Telemetry data
        ut = conn.space_center.ut
        altitude = flight.mean_altitude
        velocity = flight.velocity
        orbital_velocity = sum(v**2 for v in velocity) ** 0.5
        apoapsis = vessel.orbit.apoapsis
        periapsis = vessel.orbit.periapsis
        inclination = vessel.orbit.inclination

        # Temperatures from 2HOT Thermometers
        inside_temp = inside_thermometer.temperature
        outside_temp = outside_thermometer.temperature

        # Real-time printout
        print(f"[{ut:.1f}s] Alt: {altitude:.0f}m | V: {orbital_velocity:.1f}m/s | "
              f"Batt: {battery_percent:.1f}% | Inside: {inside_temp:.1f}K | Outside: {outside_temp:.1f}K")

        # Write to CSV
        writer.writerow([
            ut, altitude, orbital_velocity,
            apoapsis, periapsis, inclination,
            battery_percent, inside_temp, outside_temp
        ])

        # Sample rate (1 Hz)
        time.sleep(1)
