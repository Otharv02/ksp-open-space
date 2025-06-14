import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def generate_orbit_animation(csv_path, save=False):
    # Load telemetry data
    df = pd.read_csv(csv_path)

    # Orbital parameters (your input)
    semi_major_axis = 1157000
    eccentricity = 0.31
    inclination = np.radians(65.1)
    
    # Downsample for performance
    df = df.iloc[::5].reset_index(drop=True)
    num_frames = len(df)

    # Calculate orbital positions
    theta = np.linspace(0, 2 * np.pi, num_frames)
    r = (semi_major_axis * (1 - eccentricity ** 2)) / (1 + eccentricity * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta) * np.cos(inclination)

    df['x'] = x
    df['y'] = y

    # Apoapsis (max radius)
    apoapsis_index = np.argmax(r)

    # Setup figure
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor("black")
    ax.set_xlim(-1.5e6, 1.5e6)
    ax.set_ylim(-1.5e6, 1.5e6)
    ax.set_aspect('equal')
    ax.set_title("Kerbnik-1 Orbit", color='white')
    ax.tick_params(colors='white')

    # Kerbin
    kerbin = plt.Circle((0, 0), 600000, color='deepskyblue')
    ax.add_artist(kerbin)

    # Orbit path
    ax.plot(x, y, color='white', linestyle='--', linewidth=0.5)

    # Satellite marker
    sat_dot, = ax.plot([], [], 'o', color='white', markersize=6)

    # Telemetry text
    telemetry_text = ax.text(-1.45e6, 1.35e6, '', color='white', fontsize=9, verticalalignment='top')

    def animate(i):
        if i > apoapsis_index:
            return sat_dot, telemetry_text

        sat_dot.set_data([df['x'][i]], [df['y'][i]])
        telemetry = (
            f"Time: {df['Time'][i]:.1f}s\n"
            f"Altitude: {r[i] - 600000:.0f} m\n"
            f"Progress: {i / num_frames * 100:.1f}%"
        )
        telemetry_text.set_text(telemetry)
        return sat_dot, telemetry_text

    ani = animation.FuncAnimation(
        fig, animate, frames=apoapsis_index + 1, interval=50, blit=True
    )

    if save:
        print("Saving animation as GIF (this may take a minute)...")
        ani.save("orbit.gif", writer='pillow', fps=20)
        print("Saved: orbit.gif")
    else:
        plt.show()

# Entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gif.py <telemetry_csv_path> [--save]")
        sys.exit(1)

    csv_file = sys.argv[1]
    save_flag = "--save" in sys.argv
    generate_orbit_animation(csv_file, save=save_flag)
