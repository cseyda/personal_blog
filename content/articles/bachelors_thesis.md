Title: My bachelor's thesis
Date: 2011-03-28
Category: Python
Tags: pelican, publishing
Slug: bachelor-thesis
Summary: My bachelor's thesis Estimation of Power Consumption of DVFS-Enabled Processors

# Estimation of Power Consumption of DVFS-Enabled Processors
[Link to the PDF]({filename}/static/BA.pdf)

## Abstract
Saving energy is nowadays a critical factor, especially for data centers or high performance clusters which have a power consumption of several mega watts. The simple use of component energy saving mechanisms is not always possible, because this can lead to performance degradation. For this reason, high performance clusters are mainly not using them, even in low utilization phases. Modelling the power consumption of a component based on specific recordable values can help to find ways of saving energy or predicting the power consumption after replacing the component with a more efficient
one.

One of the main power consumer on a recent system is the processor. This thesis presents a model of the power consumption of a processor based on its frequency and voltage. Comparisons with real world power consumption were done to evaluate the model. Furthermore a tracing library was extended to be able to log the processor frequency and idle states if available. Using the presented model and the trace files, a power estimator has been implemented being able to estimate the power consumption of the processor in the given trace file—or a more energy efficient processor—helping to motivate the usage of power saving mechanisms and energy efficient processors, and showing the long term potential for energy saving.
