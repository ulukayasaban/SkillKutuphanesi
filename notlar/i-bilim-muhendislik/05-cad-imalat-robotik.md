# 05-cad-imalat-robotik — Bilim, Araştırma ve Mühendislik

_CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı (URDF/SRDF)_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/14**

### bambu-labs  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 100 (A)

- **Ne yapar:** Send prints to Bambu Lab printers through Bambu Connect, Bambu Lab's official app for printing from other software, or Bambu Studio. Use when the user wants to print a sliced `.gcode.3mf`, a Bambu `.gcode` or an unsliced model on a Bambu Lab printer, over Bambu Cloud or LAN. The agent opens the file in the app; the user picks the printer and starts the print there.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** otomatik

### cad  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 98 (A)

- **Ne yapar:** Create/edit parametric CAD models, organize CAD projects, export STEP/STL/3MF/GLB files, resolve prompt references, and measure geometry with cadgen. Open and visually review existing STEP/STP, STL, 3MF and GLB files in CAD Viewer.
- **Teknoloji:** git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 139 KB (SKILL.md 12.0 KB, yük orta)
- **İnceleme:** otomatik

### dfam-check  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 100 (A)

- **Ne yapar:** Measure mesh files against Design for Additive Manufacturing (DfAM) rules and report printability findings per process (FDM, SLS, SLA/DLP, metal PBF, MJF). Use when the user asks whether a part is printable, wants overhang/wall-thickness/support analysis of an `.stl`, `.obj`, `.ply`, or `.3mf` mesh, wants a build-orientation recommendation, or wants DfAM redesign guidance before slicing with `$gco
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 5.8 KB, yük kucuk)
- **İnceleme:** otomatik

### dfm  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 100 (A)

- **Ne yapar:** Design-for-manufacturing review of a part for sheet metal, CNC machining, or injection molding - bends, reliefs and flat patterns; machining access, internal corners, deep features and setups; draft, undercuts and projected area. Use when the user asks whether a part can be bent, machined or molded, asks about manufacturability or tooling, or asks for a DFM review or redesign.
- **Teknoloji:** python, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 72 KB (SKILL.md 5.6 KB, yük kucuk)
- **İnceleme:** otomatik

### dxf  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 98 (A)

- **Ne yapar:** Generate, regenerate, and validate 2D DXF drawings from Python build123d sources. Use for DXF files, `.py` drawing scripts, @dxf models, 2D profiles, outlines, templates, gaskets, panels, flat patterns, laser/plasma/waterjet cut layouts, and 2D drawing exports of CAD geometry. Open and visually review existing DXF files in CAD Viewer.
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 17.7 KB, yük orta)
- **İnceleme:** otomatik

### engineering-drawing  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 100 (A)

- **Ne yapar:** Make an engineering drawing of a part as a PDF - orthographic views with hidden lines and centre marks, real dimensions, hole callouts, notes and a title block on ISO sheets, all projected from the part's geometry so the drawing follows the model. Use when the user asks for a drawing, a dimensioned sheet, shop or manufacturing drawings, a print, or "2D views of this part".
- **Teknoloji:** python, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 7.6 KB, yük kucuk)
- **İnceleme:** otomatik

### fictiv  ·  K-Dense-AI/scientific-agent-skills @ 593377b  ·  puan 100 (A)

- **Ne yapar:** Operates Fictiv (app.fictiv.com), the on-demand manufacturing platform, end to end in the user's browser. Covers uploading CAD parts, configuring process, material, finish, threads, tolerances and inspections, getting instant or manual quotes, reading and fixing DFM feedback, choosing lead time and region, checking out and paying (card or PO), tracking orders, reordering, and troubleshooting. Appl
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★53867, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 127 KB (SKILL.md 13.9 KB, yük orta)
- **İnceleme:** otomatik

### gcode  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 100 (A)

- **Ne yapar:** Slice 3D models into printer-ready G-code with OrcaSlicer, the open-source slicer with built-in profiles for most FDM printers (Prusa, Bambu Lab, Creality, Voron and more). Use when the user wants an `.stl`, `.3mf` or `.obj` model sliced for their printer, as a sliced `.gcode.3mf` or plain `.gcode`, headless with OrcaSlicer's command line or by opening the model in OrcaSlicer. Never contacts a pri
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### lab-hardware-cad  ·  K-Dense-AI/scientific-agent-skills @ 593377b  ·  puan 100 (A)

- **Ne yapar:** Designs custom laboratory hardware as parametric build123d models and exports fabrication artifacts as STEP, STL, and DXF files - microfluidic chips and molds, optomechanical mounts and breadboard adapters, cuvette and microplate holders, tube racks, animal-behavior rigs, and 3D-printed instrument fixtures. Use when a research task needs a physical part that must mate with standardized labware, an
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★53867, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 184 KB (SKILL.md 22.3 KB, yük orta)
- **İnceleme:** otomatik

### sdf  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 98 (A)

- **Ne yapar:** SDFormat/SDF model and world authoring, validation, and simulator handoff. Use for `.sdf` files, SDFormat XML, models, worlds, links, joints, poses, frames, inertials, visual/collision geometry, mesh URIs, sensors, lights, physics, plugins, includes, Gazebo, static SDF review, or simulator-specific metadata. Do not use for signed-distance-field geometry. Open and visually review existing SDF files
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 47 KB (SKILL.md 10.6 KB, yük orta)
- **İnceleme:** otomatik

### sendcutsend  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 98 (A)

- **Ne yapar:** Review DXF and STEP/STP uploads for SendCutSend.com orders using its ordering guide, catalog, and specs. Use only for SendCutSend.com preflight reports covering upload readiness, selected material/SKU/thickness/service availability, and service-specific checks for laser cutting, CNC routing, bending, tapping, countersinking, hardware insertion, and finishing.
- **Teknoloji:** canvas, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 12.6 KB, yük orta)
- **İnceleme:** otomatik

### srdf  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 98 (A)

- **Ne yapar:** MoveIt2 SRDF authoring, validation, and planning-semantics workflow. Use when creating, editing, inspecting, or validating `.srdf` files, MoveIt planning groups, virtual joints, passive joints, end effectors, group states, disabled collisions, URDF-paired planning semantics, or SRDF handoff for live review. Use the URDF skill for robot structure and the SDF skill for simulator descriptions. Open a
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 31 KB (SKILL.md 11.7 KB, yük orta)
- **İnceleme:** otomatik

### step-parts  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 100 (A)

- **Ne yapar:** Find, evaluate, and download common purchasable CAD parts from step.parts, including named off-the-shelf actuators, servos, motors, electronics boards, connectors, screws, bolts, nuts, washers, bearings, standoffs, and other catalog components. Use when Codex needs to search the hosted step.parts catalog before creating simplified placeholder geometry, resolve fuzzy part names, standards, aliases,
- **Teknoloji:** api-anahtari, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 5.9 KB, yük kucuk)
- **İnceleme:** otomatik

### urdf  ·  earthtojake/text-to-cad @ 2f79365  ·  puan 98 (A)

- **Ne yapar:** URDF robot description authoring and validation. Use when creating, editing, inspecting, validating, or debugging `.urdf` files, robot links, joints, limits, inertials, visual/collision geometry, mesh references, frame conventions, or robot-description artifacts. Use the SRDF skill for MoveIt2 semantic groups and IK/path-planning semantics; use the CAD skill for STEP/STL/3MF/DXF/GLB outputs. Open 
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★22519, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 48 KB (SKILL.md 9.7 KB, yük orta)
- **İnceleme:** otomatik
