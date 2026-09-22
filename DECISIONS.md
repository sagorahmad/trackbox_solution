# Architectural and Engineering Decisions

1. Assumptions and Open Questions
   -Assumed synthetic video is representative of real feeds.

   -Assumed OpenCV VideoCapture is the input method.

   -Assumed missing pitch boundaries are normal due to cuts/close‑ups.

   -Open questions: accuracy requirements, latency expectations, whether reporting should stay HTTP or move to queues, storage strategy for long feeds.

2. Validation vs. Fallback
   -Fail fast: invalid config (wrong types, ranges), missing video file → pipeline stops immediately.

   -Fallback: noisy frames, missing boundaries → detector returns None, excluded from metrics, pipeline continues.

3. Performance Trade‑offs
   -Introduced frame sampling (frame_interval) to reduce expensive detection operations when processing long videos.

   -Trade‑off: fewer frames = faster throughput, but risk of missing detections. Balanced by choosing interval = 30 (process ~1 frame per second at 30fps).

-Metrics calculated only on valid detections to avoid noise.

4. AI/LLM Disclosure
   -Used AI to discuss architecture, config validation, debugging and reporting integration.
