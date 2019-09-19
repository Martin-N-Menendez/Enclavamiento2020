// IXL_TEST.h : Automatically generated header from RAILIB CodeGen

#ifndef _IXL_TEST_H
#define _IXL_TEST_H

#include"RAILIB/RAILIB.h"

//All functions return -1 if an error ocurrs


//System initialization
void IXL_TEST_Init();

//Get system data
RAILIB_TRACK_STATE_t IXL_TEST_GetTrackState(uint32_t);
RAILIB_SIGNAL_ASPECT_t IXL_TEST_GetSignalState(uint32_t);
RAILIB_CROSSING_STATE_t IXL_TEST_GetCrossingState(uint32_t);
RAILIB_SWITCH_STATE_t IXL_TEST_GetSwitchState(uint32_t);
RAILIB_SWITCH_STATE_t IXL_TEST_GetSwitchReqState(uint32_t);
RAILIB_ROUTE_STATUS_t IXL_TEST_GetRouteState(uint32_t);
uint32_t IXL_TEST_GetDeviceNum(RAILIB_INTERLOCKING_DEVICES_t);

//System commands
uint32_t IXL_TEST_SetTrackState(uint32_t,RAILIB_TRACK_STATE_t);
uint32_t IXL_TEST_RequestRoute(uint32_t);
uint32_t IXL_TEST_ReqRouteSwitches(uint32_t);
uint32_t IXL_TEST_ReqRouteCrossings(uint32_t);
uint32_t IXL_TEST_CancelRoute(uint32_t);
uint32_t IXL_TEST_Update();
uint32_t IXL_TEST_UpdateTimers();
uint32_t IXL_TEST_SetOpMode(RAILIB_ROUTE_OPMODE_t);
uint32_t IXL_TEST_SetOpModeLocal(RAILIB_ROUTE_OPMODE_t,uint32_t);
uint32_t IXL_TEST_SetSignalType(uint32_t,RAILIB_SIGNAL_TYPE_t);


#endif //_IXL_TEST_H
