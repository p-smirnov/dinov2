from dinov2.data.datasets.cell_crops import CellCrops
for split in CellCrops.Split:
    dataset = CellCrops(split=split, root="/g/huber/projects/CITEseq/CODEX/BNHL_TMA/cell_level_he_crops/64_dataset/", extra="/g/huber/projects/CITEseq/CODEX/BNHL_TMA/cell_level_he_crops/64_dataset/")
    dataset.dump_extra()
