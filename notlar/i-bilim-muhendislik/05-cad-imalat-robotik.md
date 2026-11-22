# 05-cad-imalat-robotik — Bilim, Araştırma ve Mühendislik

_CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı (URDF/SRDF)_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/19**

### bambu-labs  ·  earthtojake/text-to-cad @ 5a5dab9  ·  puan 98 (A)

- **Ne yapar:** Send prints to Bambu Lab printers through Bambu Connect, Bambu Lab's official app for printing from other software, or Bambu Studio. Use when the user wants to print a sliced `.gcode.3mf`, a Bambu `.gcode` or an unsliced model on a Bambu Lab printer, over Bambu Cloud or LAN. The agent opens the file in the app; the user picks the printer and starts the print there.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** otomatik

### cad  ·  earthtojake/text-to-cad @ 7687743  ·  puan 96 (A)

- **Ne yapar:** Designs and edits 3D CAD - parametric parts, assemblies, mechanisms and 2D cut profiles, written as build123d Python and shown live in the text-to-cad viewer. Use for any request to model, change, measure, inspect, animate, export or convert a part or a CAD file (STEP, STL, 3MF, GLB, DXF, xbf), for references and Quick Edit prompts copied from the viewer, and to check whether a part can be machine
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 188 KB (SKILL.md 14.3 KB, yük orta)
- **İnceleme:** otomatik

### dfam-check  ·  earthtojake/text-to-cad @ 5a5dab9  ·  puan 98 (A)

- **Ne yapar:** Measure mesh files against Design for Additive Manufacturing (DfAM) rules and report printability findings per process (FDM, SLS, SLA/DLP, metal PBF, MJF). Use when the user asks whether a part is printable, wants overhang/wall-thickness/support analysis of an `.stl`, `.obj`, `.ply`, or `.3mf` mesh, wants a build-orientation recommendation, or wants DfAM redesign guidance before slicing with `$gco
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 6.0 KB, yük kucuk)
- **İnceleme:** otomatik

### dfm  ·  earthtojake/text-to-cad @ 5a5dab9  ·  puan 98 (A)

- **Ne yapar:** Design-for-manufacturing review of a part for sheet metal, CNC machining, or injection molding - bends, reliefs and flat patterns; machining access, internal corners, deep features and setups; draft, undercuts and projected area. Use when the user asks whether a part can be bent, machined or molded, asks about manufacturability or tooling, or asks for a DFM review or redesign.
- **Teknoloji:** python, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 72 KB (SKILL.md 5.6 KB, yük kucuk)
- **İnceleme:** otomatik

### dxf  ·  earthtojake/text-to-cad @ 5a5dab9  ·  puan 96 (A)

- **Ne yapar:** Generates, regenerates and validates 2D DXF drawings from Python build123d models, exported by cadgen. Use for DXF files, `.py` drawing scripts, 2D profiles, outlines, templates, gaskets, panels, flat patterns, laser/plasma/waterjet cut layouts, and 2D drawing exports of CAD geometry. Opens and visually reviews existing DXF files in the CAD Viewer.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 27 KB (SKILL.md 16.6 KB, yük orta)
- **İnceleme:** otomatik

### engineering-drawing  ·  earthtojake/text-to-cad @ 7687743  ·  puan 98 (A)

- **Ne yapar:** Makes an engineering drawing of a part as a PDF, projected from its 3D geometry so the drawing follows the model, with dimensioned orthographic views, hole callouts, notes and a title block. Use when the person asks for a drawing, a dimensioned sheet, shop or manufacturing drawings, a blueprint, or "2D views of this part". Not for DXF cut layouts or flat patterns, which the cad skill makes.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 6.2 KB, yük kucuk)
- **İnceleme:** otomatik

### fea  ·  earthtojake/text-to-cad @ 7687743  ·  puan 96 (A)

- **Ne yapar:** Checks whether a part, or an assembly of bonded parts, is strong enough under its loads, as a linear static stress study (FEA). Use when the person asks whether a part will hold, break or bend too much, where it is most stressed, how much load it takes, how to make it stronger or lighter, or for FEA, a stress analysis or a strength simulation. Reports peak stress, safety factor against yield and d
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 32 KB (SKILL.md 13.4 KB, yük orta)
- **İnceleme:** otomatik

### fictiv  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Operates Fictiv (app.fictiv.com), the on-demand manufacturing platform, end to end in the user's browser. Covers uploading CAD parts, configuring process, material, finish, threads, tolerances and inspections, getting instant or manual quotes, reading and fixing DFM feedback, choosing lead time and region, checking out and paying (card or PO), tracking orders, reordering, and troubleshooting. Appl
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58028, son güncelleme 2026-11-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 127 KB (SKILL.md 13.9 KB, yük orta)
- **İnceleme:** otomatik

### gcode  ·  earthtojake/text-to-cad @ 5a5dab9  ·  puan 98 (A)

- **Ne yapar:** Slice 3D models into printer-ready G-code with OrcaSlicer, the open-source slicer with built-in profiles for most FDM printers (Prusa, Bambu Lab, Creality, Voron and more). Use when the user wants an `.stl`, `.3mf` or `.obj` model sliced for their printer, as a sliced `.gcode.3mf` or plain `.gcode`, headless with OrcaSlicer's command line or by opening the model in OrcaSlicer. Never contacts a pri
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### lab-hardware-cad  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Designs custom laboratory hardware as parametric build123d models and exports fabrication artifacts as STEP, STL, and DXF files - microfluidic chips and molds, optomechanical mounts and breadboard adapters, cuvette and microplate holders, tube racks, animal-behavior rigs, and 3D-printed instrument fixtures. Use when a research task needs a physical part that must mate with standardized labware, an
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58028, son güncelleme 2026-11-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 184 KB (SKILL.md 22.3 KB, yük orta)
- **İnceleme:** otomatik

### pcb  ·  earthtojake/text-to-cad @ 7687743  ·  puan 96 (A)

- **Ne yapar:** Designs, edits and reviews KiCad circuit boards and schematics (.kicad_pcb, .kicad_sch). Use for any request about a PCB, a schematic or a circuit - parts and nets, placement and routing, ERC and DRC, a review before ordering from JLCPCB, PCBWay or another fab, and fabrication files, a BOM, a netlist or a STEP of the board. Not for the enclosure or other mechanical parts, which the cad skill makes
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 87 KB (SKILL.md 12.6 KB, yük orta)
- **İnceleme:** otomatik

### print3d  ·  earthtojake/text-to-cad @ 7687743  ·  puan 98 (A)

- **Ne yapar:** Gets a part 3D printed - slices an .stl, .3mf or .obj into G-code with OrcaSlicer and, for a Bambu Lab printer, hands it to Bambu's own app. Use when the person wants a model sliced, printed or sent to their printer (Prusa, Bambu Lab, Creality, Voron and most FDM printers). Whether a part will print well is the cad skill's check.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 7.1 KB, yük kucuk)
- **İnceleme:** otomatik

### render  ·  earthtojake/text-to-cad @ 7687743  ·  puan 96 (A)

- **Ne yapar:** Renders photoreal images and videos of a text-to-cad model, a STEP or an xbf with Blender - a hero shot, a product or README picture, a turntable, or a film of a model's motion. Use when the person wants a picture or a video for people to look at. Not for checking geometry, which the cad skill's snapshot does.
- **Teknoloji:** node, python, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 9.5 KB, yük orta)
- **İnceleme:** otomatik

### robot-simulation  ·  earthtojake/text-to-cad @ 7687743  ·  puan 96 (A)

- **Ne yapar:** Writes and reviews robot and world descriptions (URDF, SRDF, MJCF) for ROS, MoveIt and MuJoCo. Use to generate a robot description or a MuJoCo scene from a CAD model's joints, or to write, edit or check a .urdf, .srdf or MJCF .xml by hand. Not for the CAD part itself, which the cad skill makes, and it runs no simulation.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 135 KB (SKILL.md 15.7 KB, yük orta)
- **İnceleme:** otomatik

### sdf  ·  earthtojake/text-to-cad @ 5a5dab9  ·  puan 96 (A)

- **Ne yapar:** SDFormat/SDF model and world authoring, validation, and simulator handoff. Use for `.sdf` files, SDFormat XML, models, worlds, links, joints, poses, frames, inertials, visual/collision geometry, mesh URIs, sensors, lights, physics, plugins, includes, Gazebo, static SDF review, or simulator-specific metadata. Do not use for signed-distance-field geometry. Open and visually review existing SDF files
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 54 KB (SKILL.md 12.0 KB, yük orta)
- **İnceleme:** otomatik

### sendcutsend  ·  earthtojake/text-to-cad @ 7687743  ·  puan 96 (A)

- **Ne yapar:** Checks DXF and STEP files against SendCutSend.com's ordering guide, catalog and specs before an order. Use when the person names SendCutSend or is preparing an order there, to say whether a file will upload, whether the chosen material, thickness and services are offered, and what laser cutting, CNC routing, bending, tapping, hardware or finishing require. Not for designing the part or its flat pa
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 7.9 KB, yük orta)
- **İnceleme:** otomatik

### srdf  ·  earthtojake/text-to-cad @ 5a5dab9  ·  puan 96 (A)

- **Ne yapar:** MoveIt2 SRDF authoring, validation, and planning-semantics workflow. Use when creating, editing, inspecting, or validating `.srdf` files, MoveIt planning groups, virtual joints, passive joints, end effectors, group states, disabled collisions, URDF-paired planning semantics, or SRDF handoff for live review. Use the URDF skill for robot structure and the SDF skill for simulator descriptions. Open a
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 12.4 KB, yük orta)
- **İnceleme:** otomatik

### step-parts  ·  earthtojake/text-to-cad @ 5a5dab9  ·  puan 98 (A)

- **Ne yapar:** Find, evaluate, and download common purchasable CAD parts from step.parts, including named off-the-shelf actuators, servos, motors, electronics boards, connectors, screws, bolts, nuts, washers, bearings, standoffs, and other catalog components. Use when a CAD model needs a real purchasable part: search the hosted step.parts catalog before creating simplified placeholder geometry, resolve fuzzy par
- **Teknoloji:** api-anahtari, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 6.0 KB, yük kucuk)
- **İnceleme:** otomatik

### urdf  ·  earthtojake/text-to-cad @ 5a5dab9  ·  puan 96 (A)

- **Ne yapar:** URDF robot description authoring and validation. Use when creating, editing, inspecting, validating, or debugging `.urdf` files, robot links, joints, limits, inertials, visual/collision geometry, mesh references, frame conventions, or robot-description artifacts. Use the SRDF skill for MoveIt2 semantic groups and IK/path-planning semantics; use the CAD skill for STEP/STL/3MF/DXF/GLB outputs. Open 
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** earthtojake (kisi, ★27069, son güncelleme 2026-11-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 53 KB (SKILL.md 10.8 KB, yük orta)
- **İnceleme:** otomatik
