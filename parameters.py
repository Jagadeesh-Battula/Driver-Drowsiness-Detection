import os

shape_predictor_path    = os.path.join("C:/Users/jagad/PycharmProjects/pythonProject/shape_predictor_68_face_landmarks.dat")
alarm_paths             = [os.path.join("C:/Users/jagad/PycharmProjects/pythonProject/mixkit-censorship-beep-long-1083.wav"),
                           os.path.join("C:/Users/jagad/Downloads/distraction_alert (1).wav"),
                           os.path.join("C:/Users/jagad/Downloads/distraction_alert.wav")]

EYE_DROWSINESS_THRESHOLD    = 0.25
EYE_DROWSINESS_INTERVAL     = 2.0
MOUTH_DROWSINESS_THRESHOLD  = 0.37
MOUTH_DROWSINESS_INTERVAL   = 1.0
DISTRACTION_INTERVAL        = 3.0