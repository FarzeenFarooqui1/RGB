import av
import cv2
from aiortc.contrib.media import MediaRecorder
import os

from streamlit_webrtc import VideoProcessorBase, WebRtcMode, webrtc_streamer


def record():
    class OpenCVEdgeProcessor(VideoProcessorBase):
        def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
            img = frame.to_ndarray(format="bgr24")

            return av.VideoFrame.from_ndarray(img, format="bgr24")

    def out_recorder_factory() -> MediaRecorder:
        my_path = os.path.abspath(os.path.dirname(__file__))  
        return MediaRecorder(os.path.join(my_path, "../Data/"+"output.flv"),format='flv')

    webrtc_streamer(
        key="loopback",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={
            "video": True,
            "audio": False,
        },
        video_processor_factory=OpenCVEdgeProcessor,
        out_recorder_factory=out_recorder_factory,
    )


if __name__ == "__main__":
    app()