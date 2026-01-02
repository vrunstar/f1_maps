import matplotlib.pyplot as plt
import numpy as np
import fastf1

def corner_map(season, event, session_type):
    """
    Generate a corner map for a given F1 session
    and save it to static/corner_map.png
    """
    session = fastf1.get_session(season, event, session_type)
    session.load()

    lap = session.laps.pick_fastest()
    pos = lap.get_pos_data()
    circuit_info = session.get_circuit_info()

    def rotate(xy, *, angle):
        rot_mat = np.array([[np.cos(angle), np.sin(angle)],
                            [-np.sin(angle), np.cos(angle)]])
        return np.matmul(xy, rot_mat)

    track = pos.loc[:, ('X', 'Y')].to_numpy()
    track_angle = circuit_info.rotation / 180 * np.pi
    rotated_track = rotate(track, angle=track_angle)

    plt.figure(figsize=(10, 6))
    plt.plot(rotated_track[:, 0], rotated_track[:, 1], color='red')

    offset_vector = [500, 0]

    for _, corner in circuit_info.corners.iterrows():
        txt = f"{corner['Number']}{corner['Letter']}"
        offset_angle = corner['Angle'] / 180 * np.pi
        offset_x, offset_y = rotate(offset_vector, angle=offset_angle)

        text_x = corner['X'] + offset_x
        text_y = corner['Y'] + offset_y

        text_x, text_y = rotate([text_x, text_y], angle=track_angle)
        track_x, track_y = rotate([corner['X'], corner['Y']], angle=track_angle)

        plt.scatter(text_x, text_y, color='grey', s=140)
        plt.plot([track_x, text_x], [track_y, text_y], color='grey')
        plt.text(text_x, text_y, txt, va='center_baseline', ha='center', size='small', color='white')

    plt.title(session.event['Location'], color='white')
    plt.xticks([])
    plt.yticks([])
    plt.axis('equal')
    plt.gca().set_facecolor('#050505') 

    plt.savefig("static/corner_map.png", bbox_inches='tight', facecolor='#050505')
    plt.close()
