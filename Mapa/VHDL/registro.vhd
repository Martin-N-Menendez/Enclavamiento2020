-- registro.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
	entity registro is
		port(
			Clock : in std_logic;
			procesar : in std_logic;
			procesado : out std_logic;
			paquete_i : in std_logic_vector(22-1 downto 0);
			w_data : out std_logic_vector(8-1 downto 0);
			wr_uart : out std_logic; -- "char_disp"
			Reset : in std_logic
		);
	end entity registro;
architecture Behavioral of registro is
	type estados_t is (REINICIO,CICLO_1,CICLO_2);
	signal estado, estado_siguiente : estados_t;
	signal mux_out_s,ena_s,rst_s,reg_aux : std_logic;
	signal mux_s : std_logic_vector(5-1 downto 0);
begin
	contador : process(Clock)
	begin
		if (Clock = '1' and Clock'event) then
			if Reset = '1' then
				mux_s <= "00000";
			else
				if (ena_s = '1') then
					if (mux_s /= "10110") then
						if (estado = CICLO_1 or estado = CICLO_2) then
							mux_s <= std_logic_vector(to_unsigned(to_integer(unsigned(mux_s)) + 1 , 5));
						end if;
					end if;
				end if;
				if (procesar = '0') then
					mux_s <= "00000";
				end if;
			end if;
		end if;
	end process;
	multiplexor : process(paquete_i,mux_s)
	begin
		case mux_s is
			when "00000" => mux_out_s <= paquete_i(0);
			when "00001" => mux_out_s <= paquete_i(1);
			when "00010" => mux_out_s <= paquete_i(2);
			when "00011" => mux_out_s <= paquete_i(3);
			when "00100" => mux_out_s <= paquete_i(4);
			when "00101" => mux_out_s <= paquete_i(5);
			when "00110" => mux_out_s <= paquete_i(6);
			when "00111" => mux_out_s <= paquete_i(7);
			when "01000" => mux_out_s <= paquete_i(8);
			when "01001" => mux_out_s <= paquete_i(9);
			when "01010" => mux_out_s <= paquete_i(10);
			when "01011" => mux_out_s <= paquete_i(11);
			when "01100" => mux_out_s <= paquete_i(12);
			when "01101" => mux_out_s <= paquete_i(13);
			when "01110" => mux_out_s <= paquete_i(14);
			when "01111" => mux_out_s <= paquete_i(15);
			when "10000" => mux_out_s <= paquete_i(16);
			when "10001" => mux_out_s <= paquete_i(17);
			when "10010" => mux_out_s <= paquete_i(18);
			when "10011" => mux_out_s <= paquete_i(19);
			when "10100" => mux_out_s <= paquete_i(20);
			when "10101" => mux_out_s <= paquete_i(21);
			when others => mux_out_s <= '0';
		end case;
	end process;
	w_data <= "00110001" when mux_out_s = '1' else "00110000";
	FSM_reset : process(Clock)
	begin
		if (Clock = '1' and Clock'event) then
			if Reset = '1' then
				estado <= REINICIO;
			else
				if (procesar = '1') then
					estado <= estado_siguiente;
				else
					estado <= REINICIO;
				end if;
			end if;
		end if;
	end process;
	FSM : process(procesar,estado,mux_s)
	begin
		estado_siguiente <= estado;
		case estado is
			when REINICIO =>
				wr_uart <= '0';
				rst_s <= '1';
				ena_s <= '0';
				procesado <= '0';
				reg_aux <= '0';
				if (procesar = '1' and mux_s /= "10110" ) then
					estado_siguiente <= CICLO_1;
				end if;
			when CICLO_1 =>
				wr_uart <= '0';
				rst_s <= '0';
				ena_s <= '0';
				--procesado <= '0';
				estado_siguiente <= CICLO_2;
			when CICLO_2 =>
				wr_uart <= '1';
				rst_s <= '0';
				ena_s <= '1';
				procesado <= '0';
				reg_aux <= '0';
				if mux_s = "10101" then
					procesado <= '1';
					reg_aux <= '1';
					estado_siguiente <= REINICIO;
				else
					estado_siguiente <= CICLO_1;
				end if;
			when others => null;
		end case;
	end process;
end Behavioral;