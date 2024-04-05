import argparse
import swayipc
import signal
import sys
from functools import partial

def on_window_float(ipc, event):
    window = event.container
    window.command("opacity 1")  # Maintain normal opacity
    window.set_property("_floating_blur", "true")
    # Apply blur only when the property is set to "true"
    if window.get_property("_floating_blur") == "true":
        window.command("blur 9")  # Adjust blur intensity

def on_window_unfloat(ipc, event):
    window = event.container
    window.command("opacity 1")  # Restore opacity
    window.set_property("_floating_blur", "false")
    # Remove blur only when the property is set to "false"
    if window.get_property("_floating_blur") == "false":
        window.command("blur 0")  # Remove blur effect

def stop_blurring(ipc):
    for window in ipc.get_tree():
        if window.get_property("_floating_blur") == "true":
            window.command("blur 0")
    ipc.main_quit()
    sys.exit(0)

if __name__ == "__main__":
    ipc = swayipc.Connection()

    ipc.on("window::floating", on_window_float)
    ipc.on("window::unfloating", on_window_unfloat)

    for sig in [signal.SIGINT, signal.SIGTERM]:
        signal.signal(sig, lambda signal, frame: stop_blurring(ipc))

    ipc.main()
