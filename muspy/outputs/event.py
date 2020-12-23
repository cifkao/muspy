"""Event-based representation output interface."""
from typing import Optional, TYPE_CHECKING

from numpy import ndarray

if TYPE_CHECKING:
    from ..music import Music


def to_event_representation(
    music: "Music",
    use_single_note_off_event: bool = False,
    use_end_of_sequence_event: bool = False,
    encode_velocity: bool = False,
    force_velocity_event: bool = True,
    max_time_shift: int = 100,
    velocity_bins: int = 32,
    encode_instrument: bool = False,
    encode_drum_program: bool = False,
    num_tracks: Optional[int] = None,
    ignore_empty_tracks: bool = False,
) -> ndarray:
    """Encode a Music object into event-based representation.

    The event-based represetantion represents music as a sequence of
    events, including note-on, note-off, time-shift and velocity events.
    The output shape is M x 1, where M is the number of events. The
    values encode the events. The default configuration uses 0-127 to
    encode note-on events, 128-255 for note-off events, 256-355 for
    time-shift events, and 356 to 387 for velocity events.

    Parameters
    ----------
    music : :class:`muspy.Music`
        Music object to encode.
    use_single_note_off_event : bool
        Whether to use a single note-off event for all the pitches. If
        True, the note-off event will close all active notes, which can
        lead to lossy conversion for polyphonic music. Defaults to
        False.
    use_end_of_sequence_event : bool
        Whether to append an end-of-sequence event to the encoded
        sequence. Defaults to False.
    encode_velocity : bool
        Whether to encode velocities.
    force_velocity_event : bool
        Whether to add a velocity event before every note-on event. If
        False, velocity events are only used when the note velocity is
        changed (i.e., different from the previous one). Defaults to
        True.
    max_time_shift : int
        Maximum time shift (in ticks) to be encoded as an separate
        event. Time shifts larger than `max_time_shift` will be
        decomposed into two or more time-shift events. Defaults to 100.
    velocity_bins : int
        Number of velocity bins to use. Defaults to 32.
    encode_instrument: bool
        Whether to encode the `program` and `is_drum` attributes for
        each track. Defaults to False.
    encode_drum_program: bool
        Whether to encode `program` (drum kit) for drums. Defaults to
        False, which means 0 (standard drum kit) will be used. Has no
        effect if `encode_instrument` is False.
    num_tracks: int or None
        The maximum number of tracks. Defaults to None, which means
        single-track mode (encode all events as if they were in one
        track).
    ignore_empty_tracks: bool
        Whether empty tracks should be ignored when encoding and deleted
        when decoding. Defaults to False.

    Returns
    -------
    ndarray, dtype=uint16, shape=(?, 1)
        Encoded array in event-based representation.

    """
    # Avoid circular imports
    from ..processors.event import EventRepresentationProcessor
    processor = EventRepresentationProcessor(
        use_single_note_off_event=use_single_note_off_event,
        use_end_of_sequence_event=use_end_of_sequence_event,
        encode_velocity=encode_velocity,
        force_velocity_event=force_velocity_event,
        max_time_shift=max_time_shift,
        velocity_bins=velocity_bins,
        encode_instrument=encode_instrument,
        encode_drum_program=encode_drum_program,
        num_tracks=num_tracks,
        ignore_empty_tracks=ignore_empty_tracks)
    return processor.encode(music)