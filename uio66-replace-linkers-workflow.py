import importlib.resources

from mofun import Atoms, replace_pattern_in_structure
from mofun.rough_uff import pair_params
from mofun.uff4mof import uff_key_starts_with

def assign_pair_params_to_structure(structure):
    # NOTE: in UFF, pair params should always be the same for atoms of the same element, regardless of type
    # DUPLICATE in cif2lmpdat_wcharges.py: should be refactored
    uff_keys = [uff_key_starts_with(el.ljust(2, "_"))[0] for el in structure.atom_type_elements]
    structure.pair_params = ['%10.6f %10.6f # %s' % (*pair_params(k), k) for k in uff_keys]
    structure.atom_type_labels = uff_keys

structure = Atoms.from_cif("uio66.cif")
assign_pair_params_to_structure(structure)

with open("uio66-linker.lmpdat", 'r') as f:
    linker = Atoms.from_lammps_data(f, use_comment_for_type_labels=True)
with open("uio66-linker-defect.lmpdat", 'r') as f:
    defective_linker = Atoms.from_lammps_data(f, use_comment_for_type_labels=True)

final_structure = replace_pattern_in_structure(structure, linker, linker, replace_fraction=1.0)

with open("test-defective-uio66.lmpdat", 'w') as f:
    final_structure.to_lammps_data(f)
final_structure.to_ase().write("test-defective-uio66.cif")
