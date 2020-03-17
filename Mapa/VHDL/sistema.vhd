-- Sistema.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
	entity sistema is
		port(
			Clock :  in std_logic;
			r_data :  in std_logic_vector(8-1 downto 0);
			r_disponible :  in std_logic;
			leer :  out std_logic;
			escribir :  out std_logic;
			switch1 :  in std_logic;
			switch2 :  in std_logic;
			reset_uart :  out std_logic;
			N :  in integer;
			leds :  out std_logic_vector(4-1 downto 0);
			led_rgb_1 :  out std_logic_vector(3-1 downto 0);
			led_rgb_2 :  out std_logic_vector(3-1 downto 0);
			w_data :  out std_logic_vector(8-1 downto 0);
			Reset :  in std_logic
		);
	end entity sistema;
architecture Behavioral of sistema is
	component detector is
		port(
			Clock :  in std_logic;
			r_data :  in std_logic_vector(8-1 downto 0);
			r_disponible :  in std_logic;
			led_rgb_1 :  out std_logic_vector(3-1 downto 0);
			led_rgb_2 :  out std_logic_vector(3-1 downto 0);
			paquete :  out std_logic_vector(21-1 downto 0);
			procesar :  in std_logic;
			procesado :  out std_logic;
			N :  in integer;
			wr_uart :  out std_logic;
			w_data :  out std_logic_vector(8-1 downto 0);
			Reset :  in std_logic
		);
	end component detector;
	component enclavamiento is
		port(
			Clock :  in std_logic;
			procesar :  in std_logic;
			procesado :  out std_logic;
			Paquete_i :  in std_logic_vector(21-1 downto 0);
			Paquete_o :  out std_logic_vector(15-1 downto 0);
			Reset :  in std_logic
		);
	end component enclavamiento;
	component selector is
		port(
			Clock :  in std_logic;
			switch :  in std_logic;
			leds :  out std_logic_vector(2-1 downto 0);
			wr_uart_1 :  in std_logic;
			wr_uart_2 :  in std_logic;
			wr_uart_3 :  out std_logic;
			w_data_1 :  in std_logic_vector(8-1 downto 0);
			w_data_2 :  in std_logic_vector(8-1 downto 0);
			w_data_3 :  out std_logic_vector(8-1 downto 0);
			Reset :  in std_logic
		);
	end component selector;
	component registro is
		port(
			Clock :  in std_logic;
			procesar :  in std_logic;
			procesado :  out std_logic;
			paquete_i :  in std_logic_vector(15-1 downto 0);
			w_data :  out std_logic_vector(8-1 downto 0);
			wr_uart :  out std_logic;
			Reset :  in std_logic
		);
	end component registro;
	Signal paquete_i_s : std_logic_vector(21-1 downto 0);
	Signal paquete_o_s : std_logic_vector(15-1 downto 0);
	Signal w_data_1,w_data_2,w_data_3 : std_logic_vector(8-1 downto 0);
	Signal wr_uart_1_s,wr_uart_2_s : std_logic;
	Signal pro_enc_reg,pro_det_enc,pro_reg_det : std_logic;
begin
	detector_i : detector
		port map(
			Clock => Clock,
			Reset => Reset,
			r_data => r_data,
			r_disponible => r_disponible,
			led_rgb_1 => led_rgb_1,
			led_rgb_2 => led_rgb_2,
			N => N,
			wr_uart => wr_uart_1_s,
			procesar => pro_reg_det,
			procesado => pro_det_enc,
			paquete => paquete_i_s,
			w_data => w_data_1
		);
	enclavamiento_i : enclavamiento
		port map(
			Clock => Clock,
			Reset => Reset,
			procesar => pro_det_enc,
			procesado => pro_enc_reg,
			Paquete_i => paquete_i_s,
			Paquete_o => paquete_o_s
		);
	registro_i : registro
		port map(
			Clock => Clock,
			Reset => Reset,
			procesar => pro_enc_reg,
			procesado => pro_reg_det,
			paquete_i => paquete_o_s,
			w_data => w_data_2,
			wr_uart => wr_uart_2_s
		);
	selector_i : selector
		port map(
			Clock => Clock,
			Reset => Reset,
			switch => switch1,
			wr_uart_1 => wr_uart_1_s,
			wr_uart_2 => wr_uart_2_s,
			wr_uart_3 => escribir,
			w_data_1 => w_data_1,
			w_data_2 => w_data_2,
			w_data_3 => w_data_3
		);
		w_data <= w_data_3;
		process(Clock)
		begin
			if (Clock = '1' and Clock'event) then
				if switch2 = '1' then
					leds <= std_logic_vector(to_unsigned(N,4));
				else
					leds(3) <= paquete_i_s(3);
					leds(2) <= paquete_i_s(2);
					leds(1) <= paquete_i_s(1);
					leds(0) <= paquete_i_s(0);
				end if;
			end if;
		end process;
		process(Clock)
		variable contador: integer := 0;
		begin
			if (Clock = '1' and Clock'event) then
				if Reset = '1' then
					reset_uart <= '0';
				else
					contador := contador + 1;
					if contador = 10*125E6 then
						contador := 0;
						reset_uart <= '1';
					else
						reset_uart <= '0';
					end if;
				end if;
			end if;
		end process;
end Behavioral;