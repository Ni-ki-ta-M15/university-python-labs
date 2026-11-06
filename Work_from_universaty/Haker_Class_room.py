import datetime as dt, webbrowser
import time, pyautogui
from Universaty import Automatic

while True:
    time.sleep(30)
    Day_num = Automatic.dayNumber
    # print(Day_num)
    hour_now = dt.datetime.now().time().hour
    minute_now = dt.datetime.now().time().minute
    list_times = []
    list_times.append(hour_now)
    list_times.append(minute_now)
    print(list_times)
    print(hour_now, end=':')
    print(minute_now)
    print('____________________')

    if Day_num == 1:
        if hour_now >= 8 and hour_now < 9 and minute_now >= 0 and minute_now < 10:
            print('Укр.яз лекция, открываю!')
            time.sleep(2)
            webbrowser.open('https://meet.google.com/vdr-hysi-jvf?authuser=1')
            pyautogui.sleep(10)
            pyautogui.click(587, 801)
            pyautogui.sleep(5)
            pyautogui.click(704, 784)
            time.sleep(5)
            pyautogui.click(1306, 559)
            time.sleep(5)
            pyautogui.keyDown('space')

            CHUNK = 1024

            import wave, pyaudio

            with wave.open('../../Spec file (import exe.file)/output.wav', 'rb') as wf:
                p = pyaudio.PyAudio()

                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)
                stream.close()
                p.terminate()
                time.sleep(1)
                pyautogui.keyUp('space')
                break
        if hour_now >= 9 and hour_now < 10 and minute_now >= 51 and minute_now < 58:
            print('ОАОИ лекция, открываю!')
            time.sleep(2)
            webbrowser.open_new_tab('https://meet.google.com/uqr-ymaz-dcx?authuser=1')
            pyautogui.sleep(10)
            pyautogui.click(587, 801)
            pyautogui.sleep(5)
            pyautogui.click(704, 784)
            time.sleep(5)
            pyautogui.click(1272, 616)
            time.sleep(5)
            pyautogui.keyDown('space')

            CHUNK = 1024

            import wave, pyaudio

            with wave.open('../../Spec file (import exe.file)/output.wav', 'rb') as wf:
                p = pyaudio.PyAudio()

                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)
                stream.close()
                p.terminate()
                time.sleep(1)
                pyautogui.keyUp('space')
                break
    if Day_num == 2:
        if hour_now >= 12 and hour_now < 13 and minute_now >= 21 and minute_now < 23:
            print('ВМ лекция, открываю!')
            time.sleep(2)
            webbrowser.open_new_tab('https://meet.google.com/nmd-nzjm-dqp?authuser=1&pli=1')
            pyautogui.sleep(10)
            pyautogui.click(587, 801)
            pyautogui.sleep(5)
            pyautogui.click(704, 784)
            time.sleep(5)
            pyautogui.click(1306, 559)
            time.sleep(5)
            pyautogui.keyDown('space')

            CHUNK = 1024

            import wave, pyaudio

            with wave.open('../../Spec file (import exe.file)/output.wav', 'rb') as wf:
                p = pyaudio.PyAudio()

                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)
                stream.close()
                p.terminate()
                pyautogui.keyUp('space')
            break
        if hour_now >= 13 and hour_now < 14 and minute_now >= 31 and minute_now < 35:
            print('ВМ прак., открываю!')
            time.sleep(2)
            webbrowser.open('https://meet.google.com/nmd-nzjm-dqp?authuser=1&pli=1')
            pyautogui.sleep(10)
            pyautogui.click(587, 801)
            pyautogui.sleep(5)
            pyautogui.click(704, 784)
            time.sleep(5)
            pyautogui.click(1272, 616)
            time.sleep(5)
            pyautogui.keyDown('space')

            CHUNK = 1024

            import wave, pyaudio

            with wave.open('../../Spec file (import exe.file)/output.wav', 'rb') as wf:
                p = pyaudio.PyAudio()

                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)
                stream.close()
                p.terminate()
                time.sleep(1)
                pyautogui.keyUp('space')
                break
    if Day_num == 3:
        if hour_now >= 8 and hour_now < 9 and minute_now >= 00 and minute_now < 5:
            print('ИТ практика, открываю!')
            time.sleep(2)
            webbrowser.open_new_tab('https://meet.google.com/bmp-wxwu-hmy?authuser=1')
            pyautogui.sleep(10)
            pyautogui.click(587, 801)
            pyautogui.sleep(5)
            pyautogui.click(704, 784)
            time.sleep(5)
            pyautogui.click(1324, 616)
            time.sleep(5)
            pyautogui.keyDown('space')

            CHUNK = 1024

            import wave, pyaudio

            with wave.open('../../Spec file (import exe.file)/output.wav', 'rb') as wf:
                p = pyaudio.PyAudio()

                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)
                stream.close()
                p.terminate()
                pyautogui.keyUp('space')
            break

        if hour_now >= 9 and hour_now < 10 and minute_now >= 50 and minute_now < 55:
            print('ИТ практика, открываю!')
            time.sleep(2)
            webbrowser.open_new_tab('https://meet.google.com/bmp-wxwu-hmy?authuser=1')
            pyautogui.sleep(10)
            pyautogui.click(587, 801)
            pyautogui.sleep(5)
            pyautogui.click(704, 784)
            time.sleep(5)
            pyautogui.click(1306, 559)
            time.sleep(5)
            pyautogui.keyDown('space')

            CHUNK = 1024

            import wave, pyaudio

            with wave.open('../../Spec file (import exe.file)/output.wav', 'rb') as wf:
                p = pyaudio.PyAudio()

                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)
                stream.close()
                p.terminate()
                pyautogui.keyUp('space')
            break
    if Day_num == 4:
        if hour_now >= 9 and hour_now < 10 and minute_now >= 51 and minute_now < 56:
            print('Английский, открываю!')
            time.sleep(2)
            webbrowser.open_new_tab('https://meet.google.com/cra-vpwg-vgk?authuser=1')
            pyautogui.sleep(10)
            pyautogui.click(587, 801)
            pyautogui.sleep(5)
            pyautogui.click(704, 784)
            time.sleep(5)
            pyautogui.click(1306, 559)
            time.sleep(5)
            pyautogui.keyDown('space')

            CHUNK = 1024

            import wave, pyaudio

            with wave.open('../../Spec file (import exe.file)/English.wav', 'rb') as wf:
                p = pyaudio.PyAudio()

                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)
                stream.close()
                p.terminate()
                pyautogui.keyUp('space')
            break
        if hour_now >= 11 and hour_now < 12 and minute_now >= 40 and minute_now < 45:
            print('Физика практика открываю!')
            time.sleep(2)
            webbrowser.open('https://meet.google.com/myh-cbau-axt?authuser=1&hs=179')
            pyautogui.sleep(10)
            pyautogui.click(587, 801)
            pyautogui.sleep(5)
            pyautogui.click(704, 784)
            time.sleep(5)
            pyautogui.click(1306, 559)
            time.sleep(5)
            pyautogui.keyDown('space')

            CHUNK = 1024

            import wave, pyaudio

            with wave.open('../../Spec file (import exe.file)/output.wav', 'rb') as wf:
                p = pyaudio.PyAudio()

                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)
                    stream.close()
                p.terminate()
                pyautogui.keyUp('space')
            break
    if Day_num == 5:
        if hour_now >= 8 and hour_now < 9 and minute_now >= 00 and minute_now < 5:
            print('Физика лекция, открываю!')
            time.sleep(2)
            webbrowser.open('https://meet.google.com/pym-iprr-yho?authuser=1')
            pyautogui.sleep(10)
            pyautogui.click(587, 801)
            pyautogui.sleep(5)
            pyautogui.click(704, 784)
            time.sleep(5)
            pyautogui.click(1306, 559)
            time.sleep(5)
            pyautogui.keyDown('space')

            CHUNK = 1024

            import wave, pyaudio

            with wave.open('../../Spec file (import exe.file)/output.wav', 'rb') as wf:
                p = pyaudio.PyAudio()

                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)
                stream.close()
                p.terminate()
                pyautogui.keyUp('space')
            break
        if hour_now >= 9 and hour_now < 10 and minute_now >= 50 and minute_now < 55:
            print('ИТ лекция, открываю!')
            time.sleep(2)
            webbrowser.open('https://meet.google.com/sep-nqxv-osj?authuser=1&hs=179')
            pyautogui.sleep(10)
            pyautogui.click(587, 801)
            pyautogui.sleep(5)
            pyautogui.click(704, 784)
            time.sleep(5)
            pyautogui.click(1306, 559)
            time.sleep(5)
            pyautogui.keyDown('space')

            CHUNK = 1024

            import wave, pyaudio

            with wave.open('../../Spec file (import exe.file)/output.wav', 'rb') as wf:
                p = pyaudio.PyAudio()

                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)
                stream.close()
                p.terminate()
                pyautogui.keyUp('space')
                break
        if hour_now >= 11 and hour_now < 12 and minute_now >= 40 and minute_now < 45 \
                :
            break
