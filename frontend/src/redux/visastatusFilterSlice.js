import { createSlice } from "@reduxjs/toolkit";
import { fetchVisaStatusOverview } from "./visastatusOverviewSlice";

const visastatusFilterSlice = createSlice({
    name: "visastatusFilter",
    initialState: { F: [], B: [], O: [], H: [], L: [] },
    reducers: {
        updateFilter: (state, action) => {
            const { visaType, newFilter } = action.payload;
            state[visaType] = newFilter;
        },
    },
});

const { reducer, actions } = visastatusFilterSlice;
export const { updateFilter } = actions;
export const updateFilterAndFetch = (visaType, newFilter) => async dispatch => {
    dispatch(updateFilter({ visaType, newFilter }));
    dispatch(fetchVisaStatusOverview(visaType));
    return Promise.resolve();
};

export default reducer;
