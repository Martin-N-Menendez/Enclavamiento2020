onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate /tb_registro/dut/clk_i
add wave -noupdate /tb_registro/dut/rst_i
add wave -noupdate -radix binary -radixshowbase 0 /tb_registro/dut/paquete_i
add wave -noupdate -radix ascii -radixshowbase 0 /tb_registro/dut/w_data
add wave -noupdate -radix ascii -radixshowbase 0 /tb_registro/dut/char_data
add wave -noupdate -radix binary -radixshowbase 0 /tb_registro/dut/paquete_aux
add wave -noupdate -radix unsigned -radixshowbase 0 /tb_registro/dut/contador
add wave -noupdate /tb_registro/dut/estado
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {151 ns} 0}
quietly wave cursor active 1
configure wave -namecolwidth 196
configure wave -valuecolwidth 111
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
WaveRestoreZoom {0 ns} {232 ns}
