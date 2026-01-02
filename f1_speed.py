import os
import fastf1
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

def speed(season, event, session_type, driver):
    cache_dir = "cache"
    os.makedirs(cache_dir, exist_ok=True)
    fastf1.Cache.enable_cache(cache_dir)

    if season < 2018:
        session = fastf1.get_session(season, event, session_type, backend="ergast")
    else:
        session = fastf1.get_session(season, event, session_type)

    session.load()

    lap = session.laps.pick_driver(driver).pick_fastest()
    team = lap["Team"]

    tel = lap.get_telemetry()
    speed = tel["Speed"]

    x_rot = -tel["Y"]
    y_rot = tel["X"]

    points = np.array([x_rot, y_rot]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # --- Dark theme colors ---
    outline_lc = LineCollection(segments, colors="#111111", linewidth=14)  # dark outline
    lc = LineCollection(
        segments,
        cmap="Reds",
        norm=plt.Normalize(speed.min(), speed.max()),
        linewidth=10
    )
    lc.set_array(speed)

    # --- Figure setup ---
    plt.figure(figsize=(10, 8))
    ax = plt.gca()
    ax.set_facecolor("#050505")  # dark background like dashboard
    ax.add_collection(outline_lc)
    ax.add_collection(lc)
    plt.axis("equal")
    plt.axis("off")

    # --- Colorbar in light theme ---
    cbar = plt.colorbar(lc)
    cbar.set_label("Speed (km/h)", color="white")
    cbar.ax.yaxis.set_tick_params(color='white')
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')

    # --- Title in white ---
    plt.title(f"{driver} ({team}) Speed Map\n{season} {event} {session_type}", color="white")

    # --- Save output ---
    plt.savefig("static/output.png", dpi=150, bbox_inches="tight", facecolor="#050505")
    plt.close()
