import storage
import usb_cdc
import usb_midi
import usb_hid

# On some boards, we need to give up HID to accomodate MIDI.
usb_hid.disable()
usb_midi.disable()
#storage.disable_usb_drive()
usb_cdc.enable(console=True, data=True)