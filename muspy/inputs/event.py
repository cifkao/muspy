"""Event-based representation input interface."""
from typing import Optional, TYPE_CHECKING

from numpy import ndarray

from ..music import DEFAULT_RESOLUTION
if TYPE_CHECKING:
    from ..music import Music


def from_event_representation(
    array: ndarray,
    resolution: int = DEFAULT_RESOLUTION,
    program: int = 0,
    is_drum: bool = False,
    use_single_note_off_event: bool = False,
    use_end_of_sequence_event: bool = False,
    max_time_shift: int = 100,
    velocity_bins: int = 32,
    default_velocity: int = 64,
    duplicate_note_mode: str = "fifo",
    encode_velocity: bool = False,
    force_velocity_event: bool = True,
    encode_instrument: bool = False,
    num_tracks: Optional[int] = None,
    ignore_empty_tracks: bool = False,
) -> "Music":
    """Decode event-based representation into a Music object.

    Parameters
    ----------
    array : ndarray
        Array in event-based representation to decode. Cast to integer
        if not of integer type.
    resolution : int
        Time steps per quarter note. Defaults to
        `muspy.DEFAULT_RESOLUTION`.
    program : int, optional
        Program number according to General MIDI specification [1].
        Acceptable values are 0 to 127. Defaults to 0 (Acoustic Grand
        Piano).
    is_drum : bool, optional
        A boolean indicating if it is a percussion track. Defaults to
        False.
    use_single_note_off_event : bool
        Whether to use a single note-off event for all the pitches. If
        True, a note-off event will close all active notes, which can
        lead to lossy conversion for polyphonic music. Defaults to
        False.
    use_end_of_sequence_event : bool
        Whether to append an end-of-sequence event to the encoded
        sequence. Defaults to False.
    max_time_shift : int
        Maximum time shift (in ticks) to be encoded as an separate
        event. Time shifts larger than `max_time_shift` will be
        decomposed into two or more time-shift events. Defaults to 100.
    velocity_bins : int
        Number of velocity bins to use. Defaults to 32.
    default_velocity : int
        Default velocity value to use when decoding. Defaults to 64.
    duplicate_note_mode : {'fifo', 'lifo', 'close_all'}
        Policy for dealing with duplicate notes. When a note off event
        is presetned while there are multiple correspoding note on
        events that have not yet been closed, we need a policy to decide
        which note on messages to close. This is only effective when
        `use_single_note_off_event` is False. Defaults to 'fifo'.

        - 'fifo' (first in first out): close the earliest note on
        - 'lifo' (first in first out): close the latest note on
        - 'close_all': close all note on messages
    encode_instrument: bool
        Whether to encode the `program` and `is_drum` attributes for
        each track. Defaults to False.
    num_tracks: int or None
        The maximum number of tracks. Defaults to None, which means
        single-track mode (encode all events as if they were in one
        track).
    ignore_empty_tracks: bool
        Whether empty tracks should be ignored when encoding and deleted
        when decoding. Defaults to False.

    Returns
    -------
    :class:`muspy.Music`
        Decoded Music object.

    References
    ----------
    [1] https://www.midi.org/specifications/item/gm-level-1-sound-set

    """
    # Avoid circular imports
    from ..processors.event import EventRepresentationProcessor
    processor = EventRepresentationProcessor(
        resolution=resolution,
        default_program=program,
        default_is_drum=is_drum,
        use_single_note_off_event=use_single_note_off_event,
        use_end_of_sequence_event=use_end_of_sequence_event,
        max_time_shift=max_time_shift,
        velocity_bins=velocity_bins,
        default_velocity=default_velocity,
        duplicate_note_mode=duplicate_note_mode,
        encode_velocity=encode_velocity,
        force_velocity_event=force_velocity_event,
        encode_instrument=encode_instrument,
        num_tracks=num_tracks,
        ignore_empty_tracks=ignore_empty_tracks)
    return processor.decode(array)
