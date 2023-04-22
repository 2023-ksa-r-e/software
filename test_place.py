from win32com.client import Dispatch

#장비 연결
brainrecorder = Dispatch("VisionRecorder.Application")

#뇌파 기록 시작
brainrecorder.Acquisition.StartRecording(fname)

#뇌파 trigger 전송
brainrecorder.Acquisition.SetMarker(str(trigger), ['Stimulus'])

#뇌파 기록 종료
brainrecorder.Acquisition.StopRecording()