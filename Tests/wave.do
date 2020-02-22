onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate /tb_detector/dut/clk_i
add wave -noupdate /tb_detector/dut/rst_i
add wave -noupdate -radix ascii -radixshowbase 0 /tb_detector/dut/r_data
add wave -noupdate -radix binary -radixshowbase 0 /tb_detector/dut/led_rgb_1
add wave -noupdate -radix binary -radixshowbase 0 /tb_detector/dut/led_rgb_2
add wave -noupdate -radix hexadecimal -childformat {{/tb_detector/dut/paquete(22) -radix ascii} {/tb_detector/dut/paquete(21) -radix ascii} {/tb_detector/dut/paquete(20) -radix ascii} {/tb_detector/dut/paquete(19) -radix ascii} {/tb_detector/dut/paquete(18) -radix ascii} {/tb_detector/dut/paquete(17) -radix ascii} {/tb_detector/dut/paquete(16) -radix ascii} {/tb_detector/dut/paquete(15) -radix ascii} {/tb_detector/dut/paquete(14) -radix ascii} {/tb_detector/dut/paquete(13) -radix ascii} {/tb_detector/dut/paquete(12) -radix ascii} {/tb_detector/dut/paquete(11) -radix ascii} {/tb_detector/dut/paquete(10) -radix ascii} {/tb_detector/dut/paquete(9) -radix ascii} {/tb_detector/dut/paquete(8) -radix ascii} {/tb_detector/dut/paquete(7) -radix ascii} {/tb_detector/dut/paquete(6) -radix ascii} {/tb_detector/dut/paquete(5) -radix ascii} {/tb_detector/dut/paquete(4) -radix ascii} {/tb_detector/dut/paquete(3) -radix ascii} {/tb_detector/dut/paquete(2) -radix ascii} {/tb_detector/dut/paquete(1) -radix ascii} {/tb_detector/dut/paquete(0) -radix ascii}} -radixshowbase 0 -subitemconfig {/tb_detector/dut/paquete(22) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(21) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(20) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(19) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(18) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(17) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(16) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(15) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(14) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(13) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(12) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(11) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(10) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(9) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(8) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(7) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(6) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(5) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(4) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(3) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(2) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(1) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete(0) {-radix ascii -radixshowbase 0}} /tb_detector/dut/paquete
add wave -noupdate -radix hexadecimal -childformat {{/tb_detector/dut/paquete_aux(22) -radix ascii} {/tb_detector/dut/paquete_aux(21) -radix ascii} {/tb_detector/dut/paquete_aux(20) -radix ascii} {/tb_detector/dut/paquete_aux(19) -radix ascii} {/tb_detector/dut/paquete_aux(18) -radix ascii} {/tb_detector/dut/paquete_aux(17) -radix ascii} {/tb_detector/dut/paquete_aux(16) -radix ascii} {/tb_detector/dut/paquete_aux(15) -radix ascii} {/tb_detector/dut/paquete_aux(14) -radix ascii} {/tb_detector/dut/paquete_aux(13) -radix ascii} {/tb_detector/dut/paquete_aux(12) -radix ascii} {/tb_detector/dut/paquete_aux(11) -radix ascii} {/tb_detector/dut/paquete_aux(10) -radix ascii} {/tb_detector/dut/paquete_aux(9) -radix ascii} {/tb_detector/dut/paquete_aux(8) -radix ascii} {/tb_detector/dut/paquete_aux(7) -radix ascii} {/tb_detector/dut/paquete_aux(6) -radix ascii} {/tb_detector/dut/paquete_aux(5) -radix ascii} {/tb_detector/dut/paquete_aux(4) -radix ascii} {/tb_detector/dut/paquete_aux(3) -radix ascii} {/tb_detector/dut/paquete_aux(2) -radix ascii} {/tb_detector/dut/paquete_aux(1) -radix ascii} {/tb_detector/dut/paquete_aux(0) -radix ascii}} -radixshowbase 0 -subitemconfig {/tb_detector/dut/paquete_aux(22) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(21) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(20) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(19) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(18) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(17) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(16) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(15) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(14) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(13) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(12) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(11) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(10) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(9) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(8) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(7) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(6) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(5) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(4) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(3) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(2) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(1) {-radix ascii -radixshowbase 0} /tb_detector/dut/paquete_aux(0) {-radix ascii -radixshowbase 0}} /tb_detector/dut/paquete_aux
add wave -noupdate /tb_detector/dut/paquete_ok
add wave -noupdate -radix ascii -radixshowbase 0 /tb_detector/dut/w_data
add wave -noupdate /tb_detector/dut/estado
add wave -noupdate /tb_detector/dut/estado_siguiente
add wave -noupdate -radix ascii -radixshowbase 0 /tb_detector/dut/char_data
add wave -noupdate -radix decimal -radixshowbase 0 /tb_detector/dut/contador
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {3832 ns} 0}
quietly wave cursor active 1
configure wave -namecolwidth 215
configure wave -valuecolwidth 100
configure wave -justifyvalue left
configure wave -signalnamewidth 0
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ns
update
WaveRestoreZoom {1865 ns} {4938 ns}
