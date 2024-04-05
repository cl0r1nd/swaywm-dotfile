#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import i3ipc
import signal
import sys

def set_window_transparency(ipc, opacity):
    for workspace in ipc.get_tree().workspaces():
        for window in workspace:
            window.command("opacity " + opacity)

def remove_transparency(ipc):
    set_window_transparency(ipc, "1")  # Set opacity to 1 (fully opaque)
    ipc.main_quit()
    sys.exit(0)

if __name__ == "__main__":
    transparency_val = "0.80"  # Adjust this value to control transparency

    parser = argparse.ArgumentParser(
        description="Sets transparency of all windows in Sway."
    )
    parser.add_argument(
        "--opacity",
        "-o",
        type=str,
        default=transparency_val,
        help="Set opacity value in range 0...1",
    )
    args = parser.parse_args()

    ipc = i3ipc.Connection()

    set_window_transparency(ipc, args.opacity)

    for sig in [signal.SIGINT, signal.SIGTERM]:
        signal.signal(sig, lambda signal, frame: remove_transparency(ipc))

    ipc.main()
