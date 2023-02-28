The pyECSS package
=================
[![PyPI](https://badgen.net/pypi/v/pyECSS)](https://pypi.org/project/pyECSS/)
[![Documentation](https://readthedocs.org/projects/pyecss/badge/?version=latest)](http://pyecss.readthedocs.io/en/latest/?badge=latest)


## pyECSS (Entity Component Systems in a Scenegraph)

A python, pure software design pattern based package that feaures plain and simple **E**ntities, **C**omponents and **S**ystems in a **S**cenegraph architecture.

- **Documentation:** https://pyecss.readthedocs.io
- **Source code:** https://github.com/papagiannakis/pyecss
- **Bug Reports:** https://github.com/papagiannakis/pyecss/issues

---

## **Why ECS in a Scenegraph?**:

This package is aimed as a basic behind-the-black-box implementation of the two popular notions of Scenegraphs and ECS using pure 'software design patterns'. Most modern game engines are based in either scenegraphs or some version of ECS but not in their purest form. pyECSS is an attempt to show to the interested learner a clean and simple implementation of each of them, that can be used seaprately or combined for any types of applications build on top of them: from deep learning for CG till VR systems and scientific visualization.

This is part of a complete re-write in python of the [`glGA` framework](https://diglib.eg.org/bitstream/handle/10.2312/eged.20141026.009-016/009-016.pdf?sequence=1) using a modern `Entity - Components - Systems` in a `Scenegraph` approach   which resulted in `pyECSS`.

> The following software design patterns are employed:
> - Composite, Iterator Patterns: *Entity, Component, ComponentIterator*
> - Visitor Pattern: *System*
> - Facade Pattern, Factory Method: *ECSSManager*
> - Singleton Pattern: *ECSSManager*
> - Observer, Mediator: *EventManager*

## Installation

- For `standalone` use, via `pip`

  ```
  pip install pyECSS
  ```

- For `developing`, fork this repository and run

  ```
  pip install -e . --config-settings editable_mode=strict
  ```

  in the same directory with `setup.py`.


More information can be found in [Documentation](https://pyecss.readthedocs.io) and specifically at 
[Installation](https://pyecss.readthedocs.io/en/latest/installation.html).


## Contributors

- Prof. George Papagiannakis
- Dr. Kamarianakis Manos  

---
## Licensing

pyECSS is licensed under the Apache License, Version 2.0. See
[LICENSE.txt](https://github.com/papagiannakis/pyECSS/blob/develop/LICENSE.txt) for the full license text.

---

### *Copyright 2021-2023 Dr. George Papagiannakis,  papagian@csd.uoc.gr*

### *All Rights Reserved*

### *University of Crete & Foundation for Research & Technology - Hellas (FORTH)*