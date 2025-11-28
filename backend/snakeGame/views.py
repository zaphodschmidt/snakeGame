from django.shortcuts import render
from django.http import StreamingHttpResponse
import time
import datetime

def my_datastar_view(request):
    # Check if this is a Datastar request via headers
    is_datastar = request.headers.get("Datastar-Request") or getattr(request, 'datastar_request', False)

    if is_datastar:
        # Define the generator function
        def stream_generator():
            while True:
                now = datetime.datetime.now().strftime("%H:%M:%S")
                
                # HTML fragment to swap
                payload = f"<div id='mydiv'>Updated at {now}</div>"
                
                # Manual SSE Protocol for Datastar
                # 1. Event name
                yield "event: datastar-merge-fragments\n"
                # 2. Data payload (must start with 'fragments ')
                yield f"data: fragments {payload}\n\n"
                
                time.sleep(1)

        # CRITICAL: This return must be indented inside the 'if' block
        return StreamingHttpResponse(
            stream_generator(), 
            content_type='text/event-stream'
        )

    # Standard page load (if not Datastar)
    return render(request, 'datastar_page.html')