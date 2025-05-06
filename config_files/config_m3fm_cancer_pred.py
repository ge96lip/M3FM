# model configs

modalities = 'img,txt,task'
model = 'm3fm_large'
multi_task_head = "v2"

embed_dim = 1024
# Each task can have its own head with a specific input dimension.
head_dim_dict = {
    'cancer_risk': 1024,
}
#  7 classes or regression targets for the task cancer_risk.
# 6 time bins for hazard (likelihood of event in that time bin),
# +1 “base hazard” value
task_dim_dict = {
    'cancer_risk': 7,
}

num_head_dict = {
    'cancer_risk': 1,
}

task_head_map_dict = {
    'cancer_risk': 'cancer_risk',
}

loss_weight_dict = {
    'cancer_risk': [1.0, 1.0],
}

task_base_dict = {
    'cancer_risk': -1.0,
}

gpu = 0
crop_size = [128, 448, 320]
cube_size = [16, 16, 16]
hu_range = [-1300, 150]
data_name = ['cancer_risk']
task_id = 15
model_weight = 'demo_data/model_cancer_risk.pth'
