-- uart_control.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
	entity uart_control is
		port(
			Clock :  in std_logic;
			N :  out integer;
			escribir :  in std_logic;
			vacio_in :  in std_logic;
			rd_uart :  out std_logic;
			wr_uart :  out std_logic;
			Reset :  in std_logic
		);
	end entity uart_control;
architecture Behavioral of uart_control is
begin
	lectura : process(Clock)
		variable contador_i: integer := 0;
		variable L : integer := 0;
	begin
		if (Clock = '1' and Clock'event) then
			if Reset = '1' then
				L := 0;
				rd_uart <= '0';
			elsif vacio_in = '0' then   -- Tiene datos
				contador_i := contador_i + 1;
				if contador_i = 125E3 then    -- Cuento 100 mseg
					contador_i := 0;
					rd_uart <= '1';     -- Pido el dato
					L := L + 1;
				else
					rd_uart <= '0';
				end if;
			else                    -- No tiene datos
				N <= L;
				rd_uart <= '0';
			end if;
		end if;
	end process;
	escritura : process(Clock)
		variable contador_j: integer := 0;
	begin
		if (Clock = '1' and Clock'event) then
			if Reset = '1' then
				wr_uart <= '0';
			else
				wr_uart <= escribir;
			end if;
		end if;
	end process;
end Behavioral;