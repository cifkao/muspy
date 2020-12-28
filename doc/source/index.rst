===================
MusPy documentation
===================

.. image:: https://img.shields.io/github/workflow/status/salu133445/muspy/Testing
    :target: https://github.com/salu133445/muspy/actions
    :alt: GitHub workflow
.. image:: https://img.shields.io/codecov/c/github/salu133445/muspy
    :target: https://codecov.io/gh/salu133445/muspy
    :alt: Codecov
.. image:: https://img.shields.io/github/license/salu133445/muspy
    :target: https://github.com/salu133445/muspy/blob/master/LICENSE
    :alt: GitHub license
.. image:: https://img.shields.io/github/v/release/salu133445/muspy
    :target: https://github.com/salu133445/muspy/releases
    :alt: GitHub release

MusPy is an open source Python library for symbolic music generation. It provides essential tools for developing a music generation system, including dataset management, data I/O, data preprocessing and model evaluation.


Features
========

- Dataset management system for commonly used datasets with interfaces to PyTorch and TensorFlow.
- Data I/O for common symbolic music formats (e.g., MIDI, MusicXML and ABC) and interfaces to other symbolic music libraries (e.g., music21, mido, pretty_midi and Pypianoroll).
- Implementations of common music representations for music generation, including the pitch-based, the event-based, the piano-roll and the note-based representations.
- Model evaluation tools for music generation systems, including audio rendering, score and piano-roll visualizations and objective metrics.

Here is an overview of the library.

.. image:: images/system.svg


Why MusPy
=========

A music generation pipeline usually consists of several steps: data collection, data preprocessing, model creation, model training and model evaluation.

.. image:: images/pipeline.svg
    :align: center
    :width: 400px

While some components need to be customized for each model, others can be shared across systems. For symbolic music generation in particular, a number of datasets, representations and metrics have been proposed in the literature. As a result, an easy-to-use toolkit that implements standard versions of such routines could save a great deal of time and effort and might lead to increased reproducibility.


Installation
============

To install MusPy, please run ``pip install muspy``. To build MusPy from source, please download the `source <https://github.com/salu133445/muspy/releases>`_ and run ``python setup.py install``.


Documentation
=============

Documentation is available `here <https://salu133445.github.io/muspy>`_ and as docstrings with the code.


Citing
======

Please cite the following paper if you use MusPy in a published work:

Hao-Wen Dong, Ke Chen, Julian McAuley, and Taylor Berg-Kirkpatrick, "MusPy: A Toolkit for Symbolic Music Generation," in *Proceedings of the 21st International Society for Music Information Retrieval Conference (ISMIR)*, 2020.

[`homepage <https://salu133445.github.io/muspy/>`_]
[`video <https://youtu.be/atdHMEuAYno>`_]
[`paper <https://salu133445.github.io/muspy/pdf/muspy-ismir2020-paper.pdf>`_]
[`slides <https://salu133445.github.io/muspy/pdf/muspy-ismir2020-slides.pdf>`_]
[`poster <https://salu133445.github.io/muspy/pdf/muspy-ismir2020-poster.pdf>`_]
[`arXiv <https://arxiv.org/abs/2008.01951>`_]
[`code <https://github.com/salu133445/muspy>`_]
[`documentation <https://salu133445.github.io/muspy/>`_]


Disclaimer
==========

This is a utility library that downloads and prepares public datasets. We do not host or distribute these datasets, vouch for their quality or fairness, or claim that you have license to use the dataset. It is your responsibility to determine whether you have permission to use the dataset under the dataset's license.

If you're a dataset owner and wish to update any part of it (description, citation, etc.), or do not want your dataset to be included in this library, please get in touch through a GitHub issue. Thanks for your contribution to the community!


Contents
========

.. toctree::
    :maxdepth: 2

    getting_started
    classes/index
    timing
    io/index
    datasets/index
    representations/index
    synthesis
    visualization
    metrics
    doc/index
