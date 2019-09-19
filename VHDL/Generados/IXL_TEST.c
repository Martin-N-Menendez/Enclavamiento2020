// IXL_TEST.c : Automatically generated C file from RAILIB CodeGen

#include"IXL_TEST.h"

//Main Interlocking System
RAILIB_INTERLOCKING_t IXL_TEST_ixl;

//TRACK SECTIONS
#define IXL_TEST_TR_NUM 12
RAILIB_TRACK_t IXL_TEST_tracks[IXL_TEST_TR_NUM];

//SIGNALS
#define IXL_TEST_SI_NUM 14
RAILIB_SIGNAL_t IXL_TEST_signals[IXL_TEST_SI_NUM];

//SWITCH POINTS
#define IXL_TEST_SW_NUM 1
RAILIB_SWITCH_t IXL_TEST_switches[IXL_TEST_SW_NUM];

//CROSSINGS
#define IXL_TEST_CR_NUM 1
RAILIB_CROSSING_t IXL_TEST_crossings[IXL_TEST_CR_NUM];

//ROUTES
#define IXL_TEST_RO_NUM 14
RAILIB_ROUTE_t IXL_TEST_routes[IXL_TEST_RO_NUM];

//ROUTE 1 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r1_itracks[] = {IXL_TEST_tracks+0};
#define IXL_TEST_r1_itracks_num 1

#define IXL_TEST_r1_signal (IXL_TEST_signals+0)

RAILIB_TRACK_t* IXL_TEST_r1_dtracks[] = {IXL_TEST_tracks+2};
#define IXL_TEST_r1_dtracks_num 1

RAILIB_TRACK_t* IXL_TEST_r1_ctracks[] = {IXL_TEST_tracks+4};
#define IXL_TEST_r1_ctracks_num 1

RAILIB_TRACK_t* IXL_TEST_r1_otracks[] = {};
#define IXL_TEST_r1_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r1_ottracks[] = {};
#define IXL_TEST_r1_ottracks_num 0

uint32_t IXL_TEST_r1_overdelays[] = {};

uint32_t IXL_TEST_r1_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r1_ptracks[] = {IXL_TEST_tracks+2};
#define IXL_TEST_r1_ptracks_num 1

RAILIB_ROUTE_t* IXL_TEST_r1_croutes[] = {};
#define IXL_TEST_r1_croutes_num 0

RAILIB_ROUTE_t* IXL_TEST_r1_cbroutes[] = {IXL_TEST_routes+2 ,IXL_TEST_routes+4};
#define IXL_TEST_r1_cbroutes_num 2

uint32_t IXL_TEST_r1_cancdelays[] = {5,5};

RAILIB_SWITCH_t* IXL_TEST_r1_nswitches[] = {};
#define IXL_TEST_r1_nswitches_num 0

RAILIB_SWITCH_t* IXL_TEST_r1_rswitches[] = {};
#define IXL_TEST_r1_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r1_crosslocks[] = {};
#define IXL_TEST_r1_crosslocks_num 0

//ROUTE 2 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r2_itracks[] = {IXL_TEST_tracks+1};
#define IXL_TEST_r2_itracks_num 1

#define IXL_TEST_r2_signal (IXL_TEST_signals+1)

RAILIB_TRACK_t* IXL_TEST_r2_dtracks[] = {};
#define IXL_TEST_r2_dtracks_num 0

RAILIB_TRACK_t* IXL_TEST_r2_ctracks[] = {};
#define IXL_TEST_r2_ctracks_num 0

RAILIB_TRACK_t* IXL_TEST_r2_otracks[] = {};
#define IXL_TEST_r2_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r2_ottracks[] = {};
#define IXL_TEST_r2_ottracks_num 0

uint32_t IXL_TEST_r2_overdelays[] = {};

uint32_t IXL_TEST_r2_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r2_ptracks[] = {};
#define IXL_TEST_r2_ptracks_num 0

RAILIB_ROUTE_t* IXL_TEST_r2_croutes[] = {};
#define IXL_TEST_r2_croutes_num 0

RAILIB_ROUTE_t* IXL_TEST_r2_cbroutes[] = {};
#define IXL_TEST_r2_cbroutes_num 0

uint32_t IXL_TEST_r2_cancdelays[] = {};

RAILIB_SWITCH_t* IXL_TEST_r2_nswitches[] = {};
#define IXL_TEST_r2_nswitches_num 0

RAILIB_SWITCH_t* IXL_TEST_r2_rswitches[] = {};
#define IXL_TEST_r2_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r2_crosslocks[] = {};
#define IXL_TEST_r2_crosslocks_num 0

//ROUTE 3 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r3_itracks[] = {IXL_TEST_tracks+2};
#define IXL_TEST_r3_itracks_num 1

#define IXL_TEST_r3_signal (IXL_TEST_signals+2)

RAILIB_TRACK_t* IXL_TEST_r3_dtracks[] = {IXL_TEST_tracks+4};
#define IXL_TEST_r3_dtracks_num 1

RAILIB_TRACK_t* IXL_TEST_r3_ctracks[] = {IXL_TEST_tracks+6};
#define IXL_TEST_r3_ctracks_num 1

RAILIB_TRACK_t* IXL_TEST_r3_otracks[] = {};
#define IXL_TEST_r3_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r3_ottracks[] = {};
#define IXL_TEST_r3_ottracks_num 0

uint32_t IXL_TEST_r3_overdelays[] = {};

uint32_t IXL_TEST_r3_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r3_ptracks[] = {IXL_TEST_tracks+4};
#define IXL_TEST_r3_ptracks_num 1

RAILIB_ROUTE_t* IXL_TEST_r3_croutes[] = {};
#define IXL_TEST_r3_croutes_num 0

RAILIB_ROUTE_t* IXL_TEST_r3_cbroutes[] = {IXL_TEST_routes+4 ,IXL_TEST_routes+6};
#define IXL_TEST_r3_cbroutes_num 2

uint32_t IXL_TEST_r3_cancdelays[] = {5,5};

RAILIB_SWITCH_t* IXL_TEST_r3_nswitches[] = {};
#define IXL_TEST_r3_nswitches_num 0

RAILIB_SWITCH_t* IXL_TEST_r3_rswitches[] = {};
#define IXL_TEST_r3_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r3_crosslocks[] = {};
#define IXL_TEST_r3_crosslocks_num 0

//ROUTE 4 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r4_itracks[] = {IXL_TEST_tracks+3};
#define IXL_TEST_r4_itracks_num 1

#define IXL_TEST_r4_signal (IXL_TEST_signals+3)

RAILIB_TRACK_t* IXL_TEST_r4_dtracks[] = {IXL_TEST_tracks+1};
#define IXL_TEST_r4_dtracks_num 1

RAILIB_TRACK_t* IXL_TEST_r4_ctracks[] = {};
#define IXL_TEST_r4_ctracks_num 0

RAILIB_TRACK_t* IXL_TEST_r4_otracks[] = {};
#define IXL_TEST_r4_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r4_ottracks[] = {};
#define IXL_TEST_r4_ottracks_num 0

uint32_t IXL_TEST_r4_overdelays[] = {};

uint32_t IXL_TEST_r4_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r4_ptracks[] = {IXL_TEST_tracks+1};
#define IXL_TEST_r4_ptracks_num 1

RAILIB_ROUTE_t* IXL_TEST_r4_croutes[] = {};
#define IXL_TEST_r4_croutes_num 0

RAILIB_ROUTE_t* IXL_TEST_r4_cbroutes[] = {IXL_TEST_routes+1};
#define IXL_TEST_r4_cbroutes_num 1

uint32_t IXL_TEST_r4_cancdelays[] = {5};

RAILIB_SWITCH_t* IXL_TEST_r4_nswitches[] = {};
#define IXL_TEST_r4_nswitches_num 0

RAILIB_SWITCH_t* IXL_TEST_r4_rswitches[] = {};
#define IXL_TEST_r4_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r4_crosslocks[] = {};
#define IXL_TEST_r4_crosslocks_num 0

//ROUTE 5 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r5_itracks[] = {IXL_TEST_tracks+4};
#define IXL_TEST_r5_itracks_num 1

#define IXL_TEST_r5_signal (IXL_TEST_signals+4)

RAILIB_TRACK_t* IXL_TEST_r5_dtracks[] = {IXL_TEST_tracks+6};
#define IXL_TEST_r5_dtracks_num 1

RAILIB_TRACK_t* IXL_TEST_r5_ctracks[] = {IXL_TEST_tracks+8};
#define IXL_TEST_r5_ctracks_num 1

RAILIB_TRACK_t* IXL_TEST_r5_otracks[] = {};
#define IXL_TEST_r5_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r5_ottracks[] = {};
#define IXL_TEST_r5_ottracks_num 0

uint32_t IXL_TEST_r5_overdelays[] = {};

uint32_t IXL_TEST_r5_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r5_ptracks[] = {IXL_TEST_tracks+6};
#define IXL_TEST_r5_ptracks_num 1

RAILIB_ROUTE_t* IXL_TEST_r5_croutes[] = {IXL_TEST_routes+12 ,IXL_TEST_routes+13};
#define IXL_TEST_r5_croutes_num 2

RAILIB_ROUTE_t* IXL_TEST_r5_cbroutes[] = {IXL_TEST_routes+6 ,IXL_TEST_routes+8};
#define IXL_TEST_r5_cbroutes_num 2

uint32_t IXL_TEST_r5_cancdelays[] = {5,5};

RAILIB_SWITCH_t* IXL_TEST_r5_nswitches[] = {IXL_TEST_switches+0};
#define IXL_TEST_r5_nswitches_num 1

RAILIB_SWITCH_t* IXL_TEST_r5_rswitches[] = {};
#define IXL_TEST_r5_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r5_crosslocks[] = {};
#define IXL_TEST_r5_crosslocks_num 0

//ROUTE 6 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r6_itracks[] = {IXL_TEST_tracks+5};
#define IXL_TEST_r6_itracks_num 1

#define IXL_TEST_r6_signal (IXL_TEST_signals+5)

RAILIB_TRACK_t* IXL_TEST_r6_dtracks[] = {IXL_TEST_tracks+3};
#define IXL_TEST_r6_dtracks_num 1

RAILIB_TRACK_t* IXL_TEST_r6_ctracks[] = {IXL_TEST_tracks+1};
#define IXL_TEST_r6_ctracks_num 1

RAILIB_TRACK_t* IXL_TEST_r6_otracks[] = {};
#define IXL_TEST_r6_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r6_ottracks[] = {};
#define IXL_TEST_r6_ottracks_num 0

uint32_t IXL_TEST_r6_overdelays[] = {};

uint32_t IXL_TEST_r6_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r6_ptracks[] = {IXL_TEST_tracks+3};
#define IXL_TEST_r6_ptracks_num 1

RAILIB_ROUTE_t* IXL_TEST_r6_croutes[] = {IXL_TEST_routes+12 ,IXL_TEST_routes+13};
#define IXL_TEST_r6_croutes_num 2

RAILIB_ROUTE_t* IXL_TEST_r6_cbroutes[] = {IXL_TEST_routes+3 ,IXL_TEST_routes+1};
#define IXL_TEST_r6_cbroutes_num 2

uint32_t IXL_TEST_r6_cancdelays[] = {5,5};

RAILIB_SWITCH_t* IXL_TEST_r6_nswitches[] = {IXL_TEST_switches+0};
#define IXL_TEST_r6_nswitches_num 1

RAILIB_SWITCH_t* IXL_TEST_r6_rswitches[] = {};
#define IXL_TEST_r6_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r6_crosslocks[] = {};
#define IXL_TEST_r6_crosslocks_num 0

//ROUTE 7 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r7_itracks[] = {IXL_TEST_tracks+6};
#define IXL_TEST_r7_itracks_num 1

#define IXL_TEST_r7_signal (IXL_TEST_signals+6)

RAILIB_TRACK_t* IXL_TEST_r7_dtracks[] = {IXL_TEST_tracks+8};
#define IXL_TEST_r7_dtracks_num 1

RAILIB_TRACK_t* IXL_TEST_r7_ctracks[] = {IXL_TEST_tracks+10};
#define IXL_TEST_r7_ctracks_num 1

RAILIB_TRACK_t* IXL_TEST_r7_otracks[] = {};
#define IXL_TEST_r7_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r7_ottracks[] = {};
#define IXL_TEST_r7_ottracks_num 0

uint32_t IXL_TEST_r7_overdelays[] = {};

uint32_t IXL_TEST_r7_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r7_ptracks[] = {IXL_TEST_tracks+8};
#define IXL_TEST_r7_ptracks_num 1

RAILIB_ROUTE_t* IXL_TEST_r7_croutes[] = {IXL_TEST_routes+12 ,IXL_TEST_routes+13};
#define IXL_TEST_r7_croutes_num 2

RAILIB_ROUTE_t* IXL_TEST_r7_cbroutes[] = {IXL_TEST_routes+8 ,IXL_TEST_routes+10};
#define IXL_TEST_r7_cbroutes_num 2

uint32_t IXL_TEST_r7_cancdelays[] = {5,5};

RAILIB_SWITCH_t* IXL_TEST_r7_nswitches[] = {IXL_TEST_switches+0};
#define IXL_TEST_r7_nswitches_num 1

RAILIB_SWITCH_t* IXL_TEST_r7_rswitches[] = {};
#define IXL_TEST_r7_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r7_crosslocks[] = {};
#define IXL_TEST_r7_crosslocks_num 0

//ROUTE 8 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r8_itracks[] = {IXL_TEST_tracks+7};
#define IXL_TEST_r8_itracks_num 1

#define IXL_TEST_r8_signal (IXL_TEST_signals+7)

RAILIB_TRACK_t* IXL_TEST_r8_dtracks[] = {IXL_TEST_tracks+5};
#define IXL_TEST_r8_dtracks_num 1

RAILIB_TRACK_t* IXL_TEST_r8_ctracks[] = {IXL_TEST_tracks+3};
#define IXL_TEST_r8_ctracks_num 1

RAILIB_TRACK_t* IXL_TEST_r8_otracks[] = {};
#define IXL_TEST_r8_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r8_ottracks[] = {};
#define IXL_TEST_r8_ottracks_num 0

uint32_t IXL_TEST_r8_overdelays[] = {};

uint32_t IXL_TEST_r8_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r8_ptracks[] = {IXL_TEST_tracks+5};
#define IXL_TEST_r8_ptracks_num 1

RAILIB_ROUTE_t* IXL_TEST_r8_croutes[] = {IXL_TEST_routes+12 ,IXL_TEST_routes+13};
#define IXL_TEST_r8_croutes_num 2

RAILIB_ROUTE_t* IXL_TEST_r8_cbroutes[] = {IXL_TEST_routes+5 ,IXL_TEST_routes+3};
#define IXL_TEST_r8_cbroutes_num 2

uint32_t IXL_TEST_r8_cancdelays[] = {5,5};

RAILIB_SWITCH_t* IXL_TEST_r8_nswitches[] = {IXL_TEST_switches+0};
#define IXL_TEST_r8_nswitches_num 1

RAILIB_SWITCH_t* IXL_TEST_r8_rswitches[] = {};
#define IXL_TEST_r8_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r8_crosslocks[] = {};
#define IXL_TEST_r8_crosslocks_num 0

//ROUTE 9 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r9_itracks[] = {IXL_TEST_tracks+8};
#define IXL_TEST_r9_itracks_num 1

#define IXL_TEST_r9_signal (IXL_TEST_signals+8)

RAILIB_TRACK_t* IXL_TEST_r9_dtracks[] = {IXL_TEST_tracks+10};
#define IXL_TEST_r9_dtracks_num 1

RAILIB_TRACK_t* IXL_TEST_r9_ctracks[] = {};
#define IXL_TEST_r9_ctracks_num 0

RAILIB_TRACK_t* IXL_TEST_r9_otracks[] = {};
#define IXL_TEST_r9_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r9_ottracks[] = {};
#define IXL_TEST_r9_ottracks_num 0

uint32_t IXL_TEST_r9_overdelays[] = {};

uint32_t IXL_TEST_r9_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r9_ptracks[] = {IXL_TEST_tracks+10};
#define IXL_TEST_r9_ptracks_num 1

RAILIB_ROUTE_t* IXL_TEST_r9_croutes[] = {};
#define IXL_TEST_r9_croutes_num 0

RAILIB_ROUTE_t* IXL_TEST_r9_cbroutes[] = {IXL_TEST_routes+10};
#define IXL_TEST_r9_cbroutes_num 1

uint32_t IXL_TEST_r9_cancdelays[] = {5};

RAILIB_SWITCH_t* IXL_TEST_r9_nswitches[] = {};
#define IXL_TEST_r9_nswitches_num 0

RAILIB_SWITCH_t* IXL_TEST_r9_rswitches[] = {};
#define IXL_TEST_r9_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r9_crosslocks[] = {};
#define IXL_TEST_r9_crosslocks_num 0

//ROUTE 10 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r10_itracks[] = {IXL_TEST_tracks+9};
#define IXL_TEST_r10_itracks_num 1

#define IXL_TEST_r10_signal (IXL_TEST_signals+9)

RAILIB_TRACK_t* IXL_TEST_r10_dtracks[] = {IXL_TEST_tracks+7};
#define IXL_TEST_r10_dtracks_num 1

RAILIB_TRACK_t* IXL_TEST_r10_ctracks[] = {IXL_TEST_tracks+5};
#define IXL_TEST_r10_ctracks_num 1

RAILIB_TRACK_t* IXL_TEST_r10_otracks[] = {};
#define IXL_TEST_r10_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r10_ottracks[] = {};
#define IXL_TEST_r10_ottracks_num 0

uint32_t IXL_TEST_r10_overdelays[] = {};

uint32_t IXL_TEST_r10_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r10_ptracks[] = {IXL_TEST_tracks+7};
#define IXL_TEST_r10_ptracks_num 1

RAILIB_ROUTE_t* IXL_TEST_r10_croutes[] = {};
#define IXL_TEST_r10_croutes_num 0

RAILIB_ROUTE_t* IXL_TEST_r10_cbroutes[] = {IXL_TEST_routes+7 ,IXL_TEST_routes+5};
#define IXL_TEST_r10_cbroutes_num 2

uint32_t IXL_TEST_r10_cancdelays[] = {5,5};

RAILIB_SWITCH_t* IXL_TEST_r10_nswitches[] = {};
#define IXL_TEST_r10_nswitches_num 0

RAILIB_SWITCH_t* IXL_TEST_r10_rswitches[] = {};
#define IXL_TEST_r10_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r10_crosslocks[] = {};
#define IXL_TEST_r10_crosslocks_num 0

//ROUTE 11 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r11_itracks[] = {IXL_TEST_tracks+10};
#define IXL_TEST_r11_itracks_num 1

#define IXL_TEST_r11_signal (IXL_TEST_signals+10)

RAILIB_TRACK_t* IXL_TEST_r11_dtracks[] = {};
#define IXL_TEST_r11_dtracks_num 0

RAILIB_TRACK_t* IXL_TEST_r11_ctracks[] = {};
#define IXL_TEST_r11_ctracks_num 0

RAILIB_TRACK_t* IXL_TEST_r11_otracks[] = {};
#define IXL_TEST_r11_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r11_ottracks[] = {};
#define IXL_TEST_r11_ottracks_num 0

uint32_t IXL_TEST_r11_overdelays[] = {};

uint32_t IXL_TEST_r11_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r11_ptracks[] = {};
#define IXL_TEST_r11_ptracks_num 0

RAILIB_ROUTE_t* IXL_TEST_r11_croutes[] = {};
#define IXL_TEST_r11_croutes_num 0

RAILIB_ROUTE_t* IXL_TEST_r11_cbroutes[] = {};
#define IXL_TEST_r11_cbroutes_num 0

uint32_t IXL_TEST_r11_cancdelays[] = {5,5};

RAILIB_SWITCH_t* IXL_TEST_r11_nswitches[] = {};
#define IXL_TEST_r11_nswitches_num 0

RAILIB_SWITCH_t* IXL_TEST_r11_rswitches[] = {};
#define IXL_TEST_r11_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r11_crosslocks[] = {};
#define IXL_TEST_r11_crosslocks_num 0

//ROUTE 12 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r12_itracks[] = {IXL_TEST_tracks+11};
#define IXL_TEST_r12_itracks_num 1

#define IXL_TEST_r12_signal (IXL_TEST_signals+11)

RAILIB_TRACK_t* IXL_TEST_r12_dtracks[] = {IXL_TEST_tracks+9};
#define IXL_TEST_r12_dtracks_num 1

RAILIB_TRACK_t* IXL_TEST_r12_ctracks[] = {IXL_TEST_tracks+7};
#define IXL_TEST_r12_ctracks_num 1

RAILIB_TRACK_t* IXL_TEST_r12_otracks[] = {};
#define IXL_TEST_r12_otracks_num 0

RAILIB_TRACK_t* IXL_TEST_r12_ottracks[] = {};
#define IXL_TEST_r12_ottracks_num 0

uint32_t IXL_TEST_r12_overdelays[] = {};

uint32_t IXL_TEST_r12_overtimers[] = {};

RAILIB_TRACK_t* IXL_TEST_r12_ptracks[] = {IXL_TEST_tracks+9};
#define IXL_TEST_r12_ptracks_num 1

RAILIB_ROUTE_t* IXL_TEST_r12_croutes[] = {};
#define IXL_TEST_r12_croutes_num 0

RAILIB_ROUTE_t* IXL_TEST_r12_cbroutes[] = {IXL_TEST_routes+9 ,IXL_TEST_routes+7};
#define IXL_TEST_r12_cbroutes_num 2

uint32_t IXL_TEST_r12_cancdelays[] = {5,5};

RAILIB_SWITCH_t* IXL_TEST_r12_nswitches[] = {};
#define IXL_TEST_r12_nswitches_num 0

RAILIB_SWITCH_t* IXL_TEST_r12_rswitches[] = {};
#define IXL_TEST_r12_rswitches_num 0

RAILIB_CROSSING_t* IXL_TEST_r12_crosslocks[] = {};
#define IXL_TEST_r12_crosslocks_num 0

//ROUTE 13 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r13_itracks[] = {};
#define IXL_TEST_r13_itracks_num 0

#define IXL_TEST_r13_signal (IXL_TEST_signals+12)

RAILIB_TRACK_t* IXL_TEST_r13_dtracks[] = {};
#define IXL_TEST_r13_dtracks_num 0

RAILIB_TRACK_t* IXL_TEST_r13_ctracks[] = {};
#define IXL_TEST_r13_ctracks_num 0

RAILIB_TRACK_t* IXL_TEST_r13_otracks[] = {IXL_TEST_tracks+4 ,IXL_TEST_tracks+5 ,IXL_TEST_tracks+6 ,IXL_TEST_tracks+7 ,IXL_TEST_tracks+3};
#define IXL_TEST_r13_otracks_num 5

RAILIB_TRACK_t* IXL_TEST_r13_ottracks[] = {IXL_TEST_tracks+11 ,IXL_TEST_tracks+9};
#define IXL_TEST_r13_ottracks_num 2

uint32_t IXL_TEST_r13_overdelays[] = {5,5};

uint32_t IXL_TEST_r13_overtimers[IXL_TEST_r13_ottracks_num] = {0};

RAILIB_TRACK_t* IXL_TEST_r13_ptracks[] = {};
#define IXL_TEST_r13_ptracks_num 0

RAILIB_ROUTE_t* IXL_TEST_r13_croutes[] = {IXL_TEST_routes+4 ,IXL_TEST_routes+7 ,IXL_TEST_routes+13};
#define IXL_TEST_r13_croutes_num 3

RAILIB_ROUTE_t* IXL_TEST_r13_cbroutes[] = {};
#define IXL_TEST_r13_cbroutes_num 0

uint32_t IXL_TEST_r13_cancdelays[] = {};

RAILIB_SWITCH_t* IXL_TEST_r13_nswitches[] = {};
#define IXL_TEST_r13_nswitches_num 0

RAILIB_SWITCH_t* IXL_TEST_r13_rswitches[] = {IXL_TEST_switches+0};
#define IXL_TEST_r13_rswitches_num 1

RAILIB_CROSSING_t* IXL_TEST_r13_crosslocks[] = {IXL_TEST_crossings+0};
#define IXL_TEST_r13_crosslocks_num 1

//ROUTE 14 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_r14_itracks[] = {};
#define IXL_TEST_r14_itracks_num 0

#define IXL_TEST_r14_signal (IXL_TEST_signals+13)

RAILIB_TRACK_t* IXL_TEST_r14_dtracks[] = {};
#define IXL_TEST_r14_dtracks_num 0

RAILIB_TRACK_t* IXL_TEST_r14_ctracks[] = {};
#define IXL_TEST_r14_ctracks_num 0

RAILIB_TRACK_t* IXL_TEST_r14_otracks[] = {IXL_TEST_tracks+4 ,IXL_TEST_tracks+5 ,IXL_TEST_tracks+6 ,IXL_TEST_tracks+7 ,IXL_TEST_tracks+8};
#define IXL_TEST_r14_otracks_num 5

RAILIB_TRACK_t* IXL_TEST_r14_ottracks[] = {IXL_TEST_tracks+0 ,IXL_TEST_tracks+2};
#define IXL_TEST_r14_ottracks_num 2

uint32_t IXL_TEST_r14_overdelays[] = {5,5};

uint32_t IXL_TEST_r14_overtimers[IXL_TEST_r14_ottracks_num] = {0};

RAILIB_TRACK_t* IXL_TEST_r14_ptracks[] = {};
#define IXL_TEST_r14_ptracks_num 0

RAILIB_ROUTE_t* IXL_TEST_r14_croutes[] = {IXL_TEST_routes+4 ,IXL_TEST_routes+7 ,IXL_TEST_routes+12};
#define IXL_TEST_r14_croutes_num 3

RAILIB_ROUTE_t* IXL_TEST_r14_cbroutes[] = {};
#define IXL_TEST_r14_cbroutes_num 0

uint32_t IXL_TEST_r14_cancdelays[] = {};

RAILIB_SWITCH_t* IXL_TEST_r14_nswitches[] = {};
#define IXL_TEST_r14_nswitches_num 0

RAILIB_SWITCH_t* IXL_TEST_r14_rswitches[] = {IXL_TEST_switches+0};
#define IXL_TEST_r14_rswitches_num 1

RAILIB_CROSSING_t* IXL_TEST_r14_crosslocks[] = {IXL_TEST_crossings+0};
#define IXL_TEST_r14_crosslocks_num 1

//CROSSING 1 PARAMETERS
RAILIB_TRACK_t* IXL_TEST_c1_atracks[] = {IXL_TEST_tracks+2 ,IXL_TEST_tracks+3};
#define IXL_TEST_c1_atracks_num 2

RAILIB_TRACK_t* IXL_TEST_c1_tatracks[] = {IXL_TEST_tracks+0 ,IXL_TEST_tracks+5};
#define IXL_TEST_c1_tatracks_num 2

uint32_t IXL_TEST_c1_anndelays[] = {5,5};

uint32_t IXL_TEST_c1_anntimers[IXL_TEST_c1_tatracks_num] = {0};

void IXL_TEST_Init(){

	//Interlocking creation
	RAILIB_INTERLOCKING_Create(&IXL_TEST_ixl,0);
	RAILIB_INTERLOCKING_Add(&IXL_TEST_ixl,IXL_SIGNALS,IXL_TEST_signals,IXL_TEST_SI_NUM);
	RAILIB_INTERLOCKING_Add(&IXL_TEST_ixl,IXL_ROUTES,IXL_TEST_routes,IXL_TEST_RO_NUM);
	RAILIB_INTERLOCKING_Add(&IXL_TEST_ixl,IXL_SWITCHES,IXL_TEST_switches,IXL_TEST_SW_NUM);
	RAILIB_INTERLOCKING_Add(&IXL_TEST_ixl,IXL_CROSSINGS,IXL_TEST_crossings,IXL_TEST_CR_NUM);
	RAILIB_INTERLOCKING_Add(&IXL_TEST_ixl,IXL_TRACKS,IXL_TEST_tracks,IXL_TEST_TR_NUM);
	RAILIB_INTERLOCKING_Init(&IXL_TEST_ixl);

	//Route 1 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,INTERNAL_TRACKS,IXL_TEST_r1_itracks,IXL_TEST_r1_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,ROUTE_SIGNAL,IXL_TEST_r1_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,NORMAL_SWITCHES,IXL_TEST_r1_nswitches,IXL_TEST_r1_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,REVERSE_SWITCHES,IXL_TEST_r1_rswitches,IXL_TEST_r1_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,CAUTION_TRACKS,IXL_TEST_r1_ctracks,IXL_TEST_r1_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,DANGER_TRACKS,IXL_TEST_r1_dtracks,IXL_TEST_r1_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,PROXIMITY_TRACKS,IXL_TEST_r1_ptracks,IXL_TEST_r1_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,OVERLAP_TRACKS,IXL_TEST_r1_otracks,IXL_TEST_r1_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,OVER_TEMP_TRACKS,IXL_TEST_r1_ottracks,IXL_TEST_r1_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,OVERLAP_TIMINGS,IXL_TEST_r1_overdelays,IXL_TEST_r1_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,INHIBIT_ROUTES,IXL_TEST_r1_croutes,IXL_TEST_r1_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,CANC_PROX_ROUTES,IXL_TEST_r1_cbroutes,IXL_TEST_r1_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,CANC_PROX_TIMES,IXL_TEST_r1_cancdelays,IXL_TEST_r1_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,OVERLAP_TIMERS,IXL_TEST_r1_overtimers,IXL_TEST_r1_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+0,CROSSING_LOCKS,IXL_TEST_r1_crosslocks,IXL_TEST_r1_crosslocks_num);

	//Route 2 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,INTERNAL_TRACKS,IXL_TEST_r2_itracks,IXL_TEST_r2_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,ROUTE_SIGNAL,IXL_TEST_r2_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,NORMAL_SWITCHES,IXL_TEST_r2_nswitches,IXL_TEST_r2_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,REVERSE_SWITCHES,IXL_TEST_r2_rswitches,IXL_TEST_r2_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,CAUTION_TRACKS,IXL_TEST_r2_ctracks,IXL_TEST_r2_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,DANGER_TRACKS,IXL_TEST_r2_dtracks,IXL_TEST_r2_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,PROXIMITY_TRACKS,IXL_TEST_r2_ptracks,IXL_TEST_r2_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,OVERLAP_TRACKS,IXL_TEST_r2_otracks,IXL_TEST_r2_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,OVER_TEMP_TRACKS,IXL_TEST_r2_ottracks,IXL_TEST_r2_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,OVERLAP_TIMINGS,IXL_TEST_r2_overdelays,IXL_TEST_r2_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,INHIBIT_ROUTES,IXL_TEST_r2_croutes,IXL_TEST_r2_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,CANC_PROX_ROUTES,IXL_TEST_r2_cbroutes,IXL_TEST_r2_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,CANC_PROX_TIMES,IXL_TEST_r2_cancdelays,IXL_TEST_r2_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,OVERLAP_TIMERS,IXL_TEST_r2_overtimers,IXL_TEST_r2_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+1,CROSSING_LOCKS,IXL_TEST_r2_crosslocks,IXL_TEST_r2_crosslocks_num);

	//Route 3 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,INTERNAL_TRACKS,IXL_TEST_r3_itracks,IXL_TEST_r3_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,ROUTE_SIGNAL,IXL_TEST_r3_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,NORMAL_SWITCHES,IXL_TEST_r3_nswitches,IXL_TEST_r3_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,REVERSE_SWITCHES,IXL_TEST_r3_rswitches,IXL_TEST_r3_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,CAUTION_TRACKS,IXL_TEST_r3_ctracks,IXL_TEST_r3_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,DANGER_TRACKS,IXL_TEST_r3_dtracks,IXL_TEST_r3_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,PROXIMITY_TRACKS,IXL_TEST_r3_ptracks,IXL_TEST_r3_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,OVERLAP_TRACKS,IXL_TEST_r3_otracks,IXL_TEST_r3_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,OVER_TEMP_TRACKS,IXL_TEST_r3_ottracks,IXL_TEST_r3_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,OVERLAP_TIMINGS,IXL_TEST_r3_overdelays,IXL_TEST_r3_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,INHIBIT_ROUTES,IXL_TEST_r3_croutes,IXL_TEST_r3_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,CANC_PROX_ROUTES,IXL_TEST_r3_cbroutes,IXL_TEST_r3_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,CANC_PROX_TIMES,IXL_TEST_r3_cancdelays,IXL_TEST_r3_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,OVERLAP_TIMERS,IXL_TEST_r3_overtimers,IXL_TEST_r3_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+2,CROSSING_LOCKS,IXL_TEST_r3_crosslocks,IXL_TEST_r3_crosslocks_num);

	//Route 4 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,INTERNAL_TRACKS,IXL_TEST_r4_itracks,IXL_TEST_r4_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,ROUTE_SIGNAL,IXL_TEST_r4_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,NORMAL_SWITCHES,IXL_TEST_r4_nswitches,IXL_TEST_r4_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,REVERSE_SWITCHES,IXL_TEST_r4_rswitches,IXL_TEST_r4_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,CAUTION_TRACKS,IXL_TEST_r4_ctracks,IXL_TEST_r4_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,DANGER_TRACKS,IXL_TEST_r4_dtracks,IXL_TEST_r4_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,PROXIMITY_TRACKS,IXL_TEST_r4_ptracks,IXL_TEST_r4_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,OVERLAP_TRACKS,IXL_TEST_r4_otracks,IXL_TEST_r4_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,OVER_TEMP_TRACKS,IXL_TEST_r4_ottracks,IXL_TEST_r4_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,OVERLAP_TIMINGS,IXL_TEST_r4_overdelays,IXL_TEST_r4_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,INHIBIT_ROUTES,IXL_TEST_r4_croutes,IXL_TEST_r4_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,CANC_PROX_ROUTES,IXL_TEST_r4_cbroutes,IXL_TEST_r4_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,CANC_PROX_TIMES,IXL_TEST_r4_cancdelays,IXL_TEST_r4_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,OVERLAP_TIMERS,IXL_TEST_r4_overtimers,IXL_TEST_r4_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+3,CROSSING_LOCKS,IXL_TEST_r4_crosslocks,IXL_TEST_r4_crosslocks_num);

	//Route 5 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,INTERNAL_TRACKS,IXL_TEST_r5_itracks,IXL_TEST_r5_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,ROUTE_SIGNAL,IXL_TEST_r5_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,NORMAL_SWITCHES,IXL_TEST_r5_nswitches,IXL_TEST_r5_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,REVERSE_SWITCHES,IXL_TEST_r5_rswitches,IXL_TEST_r5_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,CAUTION_TRACKS,IXL_TEST_r5_ctracks,IXL_TEST_r5_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,DANGER_TRACKS,IXL_TEST_r5_dtracks,IXL_TEST_r5_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,PROXIMITY_TRACKS,IXL_TEST_r5_ptracks,IXL_TEST_r5_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,OVERLAP_TRACKS,IXL_TEST_r5_otracks,IXL_TEST_r5_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,OVER_TEMP_TRACKS,IXL_TEST_r5_ottracks,IXL_TEST_r5_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,OVERLAP_TIMINGS,IXL_TEST_r5_overdelays,IXL_TEST_r5_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,INHIBIT_ROUTES,IXL_TEST_r5_croutes,IXL_TEST_r5_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,CANC_PROX_ROUTES,IXL_TEST_r5_cbroutes,IXL_TEST_r5_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,CANC_PROX_TIMES,IXL_TEST_r5_cancdelays,IXL_TEST_r5_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,OVERLAP_TIMERS,IXL_TEST_r5_overtimers,IXL_TEST_r5_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+4,CROSSING_LOCKS,IXL_TEST_r5_crosslocks,IXL_TEST_r5_crosslocks_num);

	//Route 6 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,INTERNAL_TRACKS,IXL_TEST_r6_itracks,IXL_TEST_r6_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,ROUTE_SIGNAL,IXL_TEST_r6_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,NORMAL_SWITCHES,IXL_TEST_r6_nswitches,IXL_TEST_r6_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,REVERSE_SWITCHES,IXL_TEST_r6_rswitches,IXL_TEST_r6_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,CAUTION_TRACKS,IXL_TEST_r6_ctracks,IXL_TEST_r6_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,DANGER_TRACKS,IXL_TEST_r6_dtracks,IXL_TEST_r6_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,PROXIMITY_TRACKS,IXL_TEST_r6_ptracks,IXL_TEST_r6_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,OVERLAP_TRACKS,IXL_TEST_r6_otracks,IXL_TEST_r6_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,OVER_TEMP_TRACKS,IXL_TEST_r6_ottracks,IXL_TEST_r6_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,OVERLAP_TIMINGS,IXL_TEST_r6_overdelays,IXL_TEST_r6_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,INHIBIT_ROUTES,IXL_TEST_r6_croutes,IXL_TEST_r6_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,CANC_PROX_ROUTES,IXL_TEST_r6_cbroutes,IXL_TEST_r6_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,CANC_PROX_TIMES,IXL_TEST_r6_cancdelays,IXL_TEST_r6_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,OVERLAP_TIMERS,IXL_TEST_r6_overtimers,IXL_TEST_r6_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+5,CROSSING_LOCKS,IXL_TEST_r6_crosslocks,IXL_TEST_r6_crosslocks_num);

	//Route 7 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,INTERNAL_TRACKS,IXL_TEST_r7_itracks,IXL_TEST_r7_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,ROUTE_SIGNAL,IXL_TEST_r7_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,NORMAL_SWITCHES,IXL_TEST_r7_nswitches,IXL_TEST_r7_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,REVERSE_SWITCHES,IXL_TEST_r7_rswitches,IXL_TEST_r7_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,CAUTION_TRACKS,IXL_TEST_r7_ctracks,IXL_TEST_r7_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,DANGER_TRACKS,IXL_TEST_r7_dtracks,IXL_TEST_r7_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,PROXIMITY_TRACKS,IXL_TEST_r7_ptracks,IXL_TEST_r7_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,OVERLAP_TRACKS,IXL_TEST_r7_otracks,IXL_TEST_r7_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,OVER_TEMP_TRACKS,IXL_TEST_r7_ottracks,IXL_TEST_r7_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,OVERLAP_TIMINGS,IXL_TEST_r7_overdelays,IXL_TEST_r7_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,INHIBIT_ROUTES,IXL_TEST_r7_croutes,IXL_TEST_r7_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,CANC_PROX_ROUTES,IXL_TEST_r7_cbroutes,IXL_TEST_r7_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,CANC_PROX_TIMES,IXL_TEST_r7_cancdelays,IXL_TEST_r7_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,OVERLAP_TIMERS,IXL_TEST_r7_overtimers,IXL_TEST_r7_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+6,CROSSING_LOCKS,IXL_TEST_r7_crosslocks,IXL_TEST_r7_crosslocks_num);

	//Route 8 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,INTERNAL_TRACKS,IXL_TEST_r8_itracks,IXL_TEST_r8_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,ROUTE_SIGNAL,IXL_TEST_r8_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,NORMAL_SWITCHES,IXL_TEST_r8_nswitches,IXL_TEST_r8_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,REVERSE_SWITCHES,IXL_TEST_r8_rswitches,IXL_TEST_r8_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,CAUTION_TRACKS,IXL_TEST_r8_ctracks,IXL_TEST_r8_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,DANGER_TRACKS,IXL_TEST_r8_dtracks,IXL_TEST_r8_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,PROXIMITY_TRACKS,IXL_TEST_r8_ptracks,IXL_TEST_r8_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,OVERLAP_TRACKS,IXL_TEST_r8_otracks,IXL_TEST_r8_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,OVER_TEMP_TRACKS,IXL_TEST_r8_ottracks,IXL_TEST_r8_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,OVERLAP_TIMINGS,IXL_TEST_r8_overdelays,IXL_TEST_r8_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,INHIBIT_ROUTES,IXL_TEST_r8_croutes,IXL_TEST_r8_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,CANC_PROX_ROUTES,IXL_TEST_r8_cbroutes,IXL_TEST_r8_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,CANC_PROX_TIMES,IXL_TEST_r8_cancdelays,IXL_TEST_r8_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,OVERLAP_TIMERS,IXL_TEST_r8_overtimers,IXL_TEST_r8_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+7,CROSSING_LOCKS,IXL_TEST_r8_crosslocks,IXL_TEST_r8_crosslocks_num);

	//Route 9 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,INTERNAL_TRACKS,IXL_TEST_r9_itracks,IXL_TEST_r9_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,ROUTE_SIGNAL,IXL_TEST_r9_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,NORMAL_SWITCHES,IXL_TEST_r9_nswitches,IXL_TEST_r9_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,REVERSE_SWITCHES,IXL_TEST_r9_rswitches,IXL_TEST_r9_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,CAUTION_TRACKS,IXL_TEST_r9_ctracks,IXL_TEST_r9_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,DANGER_TRACKS,IXL_TEST_r9_dtracks,IXL_TEST_r9_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,PROXIMITY_TRACKS,IXL_TEST_r9_ptracks,IXL_TEST_r9_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,OVERLAP_TRACKS,IXL_TEST_r9_otracks,IXL_TEST_r9_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,OVER_TEMP_TRACKS,IXL_TEST_r9_ottracks,IXL_TEST_r9_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,OVERLAP_TIMINGS,IXL_TEST_r9_overdelays,IXL_TEST_r9_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,INHIBIT_ROUTES,IXL_TEST_r9_croutes,IXL_TEST_r9_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,CANC_PROX_ROUTES,IXL_TEST_r9_cbroutes,IXL_TEST_r9_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,CANC_PROX_TIMES,IXL_TEST_r9_cancdelays,IXL_TEST_r9_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,OVERLAP_TIMERS,IXL_TEST_r9_overtimers,IXL_TEST_r9_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+8,CROSSING_LOCKS,IXL_TEST_r9_crosslocks,IXL_TEST_r9_crosslocks_num);

	//Route 10 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,INTERNAL_TRACKS,IXL_TEST_r10_itracks,IXL_TEST_r10_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,ROUTE_SIGNAL,IXL_TEST_r10_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,NORMAL_SWITCHES,IXL_TEST_r10_nswitches,IXL_TEST_r10_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,REVERSE_SWITCHES,IXL_TEST_r10_rswitches,IXL_TEST_r10_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,CAUTION_TRACKS,IXL_TEST_r10_ctracks,IXL_TEST_r10_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,DANGER_TRACKS,IXL_TEST_r10_dtracks,IXL_TEST_r10_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,PROXIMITY_TRACKS,IXL_TEST_r10_ptracks,IXL_TEST_r10_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,OVERLAP_TRACKS,IXL_TEST_r10_otracks,IXL_TEST_r10_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,OVER_TEMP_TRACKS,IXL_TEST_r10_ottracks,IXL_TEST_r10_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,OVERLAP_TIMINGS,IXL_TEST_r10_overdelays,IXL_TEST_r10_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,INHIBIT_ROUTES,IXL_TEST_r10_croutes,IXL_TEST_r10_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,CANC_PROX_ROUTES,IXL_TEST_r10_cbroutes,IXL_TEST_r10_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,CANC_PROX_TIMES,IXL_TEST_r10_cancdelays,IXL_TEST_r10_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,OVERLAP_TIMERS,IXL_TEST_r10_overtimers,IXL_TEST_r10_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+9,CROSSING_LOCKS,IXL_TEST_r10_crosslocks,IXL_TEST_r10_crosslocks_num);

	//Route 11 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,INTERNAL_TRACKS,IXL_TEST_r11_itracks,IXL_TEST_r11_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,ROUTE_SIGNAL,IXL_TEST_r11_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,NORMAL_SWITCHES,IXL_TEST_r11_nswitches,IXL_TEST_r11_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,REVERSE_SWITCHES,IXL_TEST_r11_rswitches,IXL_TEST_r11_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,CAUTION_TRACKS,IXL_TEST_r11_ctracks,IXL_TEST_r11_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,DANGER_TRACKS,IXL_TEST_r11_dtracks,IXL_TEST_r11_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,PROXIMITY_TRACKS,IXL_TEST_r11_ptracks,IXL_TEST_r11_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,OVERLAP_TRACKS,IXL_TEST_r11_otracks,IXL_TEST_r11_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,OVER_TEMP_TRACKS,IXL_TEST_r11_ottracks,IXL_TEST_r11_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,OVERLAP_TIMINGS,IXL_TEST_r11_overdelays,IXL_TEST_r11_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,INHIBIT_ROUTES,IXL_TEST_r11_croutes,IXL_TEST_r11_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,CANC_PROX_ROUTES,IXL_TEST_r11_cbroutes,IXL_TEST_r11_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,CANC_PROX_TIMES,IXL_TEST_r11_cancdelays,IXL_TEST_r11_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,OVERLAP_TIMERS,IXL_TEST_r11_overtimers,IXL_TEST_r11_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+10,CROSSING_LOCKS,IXL_TEST_r11_crosslocks,IXL_TEST_r11_crosslocks_num);

	//Route 12 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,INTERNAL_TRACKS,IXL_TEST_r12_itracks,IXL_TEST_r12_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,ROUTE_SIGNAL,IXL_TEST_r12_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,NORMAL_SWITCHES,IXL_TEST_r12_nswitches,IXL_TEST_r12_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,REVERSE_SWITCHES,IXL_TEST_r12_rswitches,IXL_TEST_r12_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,CAUTION_TRACKS,IXL_TEST_r12_ctracks,IXL_TEST_r12_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,DANGER_TRACKS,IXL_TEST_r12_dtracks,IXL_TEST_r12_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,PROXIMITY_TRACKS,IXL_TEST_r12_ptracks,IXL_TEST_r12_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,OVERLAP_TRACKS,IXL_TEST_r12_otracks,IXL_TEST_r12_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,OVER_TEMP_TRACKS,IXL_TEST_r12_ottracks,IXL_TEST_r12_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,OVERLAP_TIMINGS,IXL_TEST_r12_overdelays,IXL_TEST_r12_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,INHIBIT_ROUTES,IXL_TEST_r12_croutes,IXL_TEST_r12_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,CANC_PROX_ROUTES,IXL_TEST_r12_cbroutes,IXL_TEST_r12_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,CANC_PROX_TIMES,IXL_TEST_r12_cancdelays,IXL_TEST_r12_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,OVERLAP_TIMERS,IXL_TEST_r12_overtimers,IXL_TEST_r12_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+11,CROSSING_LOCKS,IXL_TEST_r12_crosslocks,IXL_TEST_r12_crosslocks_num);

	//Route 13 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,INTERNAL_TRACKS,IXL_TEST_r13_itracks,IXL_TEST_r13_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,ROUTE_SIGNAL,IXL_TEST_r13_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,NORMAL_SWITCHES,IXL_TEST_r13_nswitches,IXL_TEST_r13_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,REVERSE_SWITCHES,IXL_TEST_r13_rswitches,IXL_TEST_r13_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,CAUTION_TRACKS,IXL_TEST_r13_ctracks,IXL_TEST_r13_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,DANGER_TRACKS,IXL_TEST_r13_dtracks,IXL_TEST_r13_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,PROXIMITY_TRACKS,IXL_TEST_r13_ptracks,IXL_TEST_r13_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,OVERLAP_TRACKS,IXL_TEST_r13_otracks,IXL_TEST_r13_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,OVER_TEMP_TRACKS,IXL_TEST_r13_ottracks,IXL_TEST_r13_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,OVERLAP_TIMINGS,IXL_TEST_r13_overdelays,IXL_TEST_r13_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,INHIBIT_ROUTES,IXL_TEST_r13_croutes,IXL_TEST_r13_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,CANC_PROX_ROUTES,IXL_TEST_r13_cbroutes,IXL_TEST_r13_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,CANC_PROX_TIMES,IXL_TEST_r13_cancdelays,IXL_TEST_r13_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,OVERLAP_TIMERS,IXL_TEST_r13_overtimers,IXL_TEST_r13_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+12,CROSSING_LOCKS,IXL_TEST_r13_crosslocks,IXL_TEST_r13_crosslocks_num);

	//Route 14 connections
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,INTERNAL_TRACKS,IXL_TEST_r14_itracks,IXL_TEST_r14_itracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,ROUTE_SIGNAL,IXL_TEST_r14_signal,1);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,NORMAL_SWITCHES,IXL_TEST_r14_nswitches,IXL_TEST_r14_nswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,REVERSE_SWITCHES,IXL_TEST_r14_rswitches,IXL_TEST_r14_rswitches_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,CAUTION_TRACKS,IXL_TEST_r14_ctracks,IXL_TEST_r14_ctracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,DANGER_TRACKS,IXL_TEST_r14_dtracks,IXL_TEST_r14_dtracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,PROXIMITY_TRACKS,IXL_TEST_r14_ptracks,IXL_TEST_r14_ptracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,OVERLAP_TRACKS,IXL_TEST_r14_otracks,IXL_TEST_r14_otracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,OVER_TEMP_TRACKS,IXL_TEST_r14_ottracks,IXL_TEST_r14_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,OVERLAP_TIMINGS,IXL_TEST_r14_overdelays,IXL_TEST_r14_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,INHIBIT_ROUTES,IXL_TEST_r14_croutes,IXL_TEST_r14_croutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,CANC_PROX_ROUTES,IXL_TEST_r14_cbroutes,IXL_TEST_r14_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,CANC_PROX_TIMES,IXL_TEST_r14_cancdelays,IXL_TEST_r14_cbroutes_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,OVERLAP_TIMERS,IXL_TEST_r14_overtimers,IXL_TEST_r14_ottracks_num);
	RAILIB_ROUTE_Connect(IXL_TEST_routes+13,CROSSING_LOCKS,IXL_TEST_r14_crosslocks,IXL_TEST_r14_crosslocks_num);

	//Crossing 1 connections
	RAILIB_CROSSING_Connect(IXL_TEST_crossings+0,ANNOUNCEMENT_TRACKS,IXL_TEST_c1_atracks,IXL_TEST_c1_atracks_num);
	RAILIB_CROSSING_Connect(IXL_TEST_crossings+0,TEMP_ANNOUNCEMENT_TRACKS,IXL_TEST_c1_tatracks,IXL_TEST_c1_tatracks_num);
	RAILIB_CROSSING_Connect(IXL_TEST_crossings+0,ANNOUNCEMENT_TIMINGS,IXL_TEST_c1_anndelays,IXL_TEST_c1_tatracks_num);
	RAILIB_CROSSING_Connect(IXL_TEST_crossings+0,ANNOUNCEMENT_TIMERS,IXL_TEST_c1_anntimers,IXL_TEST_c1_tatracks_num);

}

RAILIB_TRACK_STATE_t IXL_TEST_GetTrackState(uint32_t index){
                    
	if(index>IXL_TEST_TR_NUM){                    
		return -1;                    
	}else{                    
		return RAILIB_TRACK_GetState(IXL_TEST_tracks + index-1);
	}
}

RAILIB_SIGNAL_ASPECT_t IXL_TEST_GetSignalState(uint32_t index){
                    
	if(index>IXL_TEST_SI_NUM){                    
		return -1;                    
	}else{                    
		return RAILIB_SIGNAL_GetAspect(IXL_TEST_signals + index-1);
	}
}

RAILIB_CROSSING_STATE_t IXL_TEST_GetCrossingState(uint32_t index){
                    
	if(index>IXL_TEST_CR_NUM){                    
		return -1;                    
	}else{                    
		return RAILIB_CROSSING_GetState(IXL_TEST_crossings + index-1);
	}
}

RAILIB_SWITCH_STATE_t IXL_TEST_GetSwitchState(uint32_t index){
                    
	if(index>IXL_TEST_SW_NUM){                    
		return -1;                    
	}else{                    
		return RAILIB_SWITCH_GetState(IXL_TEST_switches + index-1);
	}
}

RAILIB_SWITCH_STATE_t IXL_TEST_GetSwitchReqState(uint32_t index){
                    
	if(index>IXL_TEST_SW_NUM){                    
		return -1;                    
	}else{                    
		return RAILIB_SWITCH_GetReqState(IXL_TEST_switches + index-1);
	}
}

RAILIB_ROUTE_STATUS_t IXL_TEST_GetRouteState(uint32_t index){
                    
	if(index>IXL_TEST_RO_NUM){                    
		return -1;                    
	}else{                    
		return RAILIB_ROUTE_GetStatus(IXL_TEST_routes + index-1);
	}
}

uint32_t IXL_TEST_SetTrackState(uint32_t index, RAILIB_TRACK_STATE_t state){
                    
	if(index>IXL_TEST_TR_NUM){                    
		return -1;                    
	}else{                    
		RAILIB_TRACK_SetState(IXL_TEST_tracks + index-1,state);                    
	return 1;

	}
}
uint32_t IXL_TEST_RequestRoute(uint32_t index){
                    
	if(index>IXL_TEST_RO_NUM){                    
		return -1;                    
	}else{                    
		return RAILIB_ROUTE_Request(IXL_TEST_routes + index-1);
	}
}

uint32_t IXL_TEST_ReqRouteSwitches(uint32_t index){
                    
	if(index>IXL_TEST_RO_NUM){                    
		return -1;                    
	}else{                    
		RAILIB_ROUTE_ReqSwitches(IXL_TEST_routes + index-1);                    
		return 1;
	}
}

uint32_t IXL_TEST_ReqRouteCrossings(uint32_t index){
                    
	if(index>IXL_TEST_RO_NUM){                    
		return -1;                    
	}else{                    
		RAILIB_ROUTE_ReqCrossings(IXL_TEST_routes + index-1);                    
		return 1;
	}
}

uint32_t IXL_TEST_CancelRoute(uint32_t index){
                    
	if(index>IXL_TEST_RO_NUM){                    
		return -1;                    
	}else{                    
		RAILIB_ROUTE_CancelRequest(IXL_TEST_routes + index-1);                    
		return 1;
	}
}

uint32_t IXL_TEST_Update(){                    
	RAILIB_INTERLOCKING_Update(&IXL_TEST_ixl);
	return 1;
}

uint32_t IXL_TEST_UpdateTimers(){                    
	RAILIB_INTERLOCKING_UpdateTimers(&IXL_TEST_ixl);
	return 1;
}

uint32_t IXL_TEST_SetOpMode(RAILIB_ROUTE_OPMODE_t mode){                    
	RAILIB_INTERLOCKING_SetOpmode(&IXL_TEST_ixl, mode);
	return 1;
}

uint32_t IXL_TEST_SetOpModeLocal(RAILIB_ROUTE_OPMODE_t mode, uint32_t route){
                    
	if(route>IXL_TEST_RO_NUM){                    
		return -1;                    
	}else{                    
		RAILIB_INTERLOCKING_SetLocalOpmode(&IXL_TEST_ixl,mode,route-1);                    
		return 1;
	}
}

uint32_t IXL_TEST_GetDeviceNum(RAILIB_INTERLOCKING_DEVICES_t type){                    
	switch(type){                    
		case IXL_ROUTES :                    
			return IXL_TEST_RO_NUM;                    
		break;                    
		case IXL_SIGNALS :                    
			return IXL_TEST_SI_NUM;                    
		break;                    
		case IXL_TRACKS :                    
			return IXL_TEST_TR_NUM;                    
		break;                    
		case IXL_SWITCHES :                    
			return IXL_TEST_SW_NUM;                    
		break;                    
		case IXL_CROSSINGS :                    
			return IXL_TEST_CR_NUM;                    
		break;                    
		default :                    
			return -1;                    
		break;                    
	}                    
}

uint32_t IXL_TEST_SetSignalType(uint32_t index, RAILIB_SIGNAL_TYPE_t type){
                    
	if(index>IXL_TEST_SI_NUM){                    
		return -1;                    
	}else{                    
		RAILIB_SIGNAL_SetType(IXL_TEST_signals + index-1,type);                    
		return 1;
	}
	return 1;
}

