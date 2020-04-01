-- cambio_11.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity cambio_11 is
		generic(
			N : natural := 90;
			N_SEM : natural := 27;
			N_MDC : natural := 12;
			N_CVS : natural := 24
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_ante_i :  in std_logic;
			Estado_post_i :  in std_logic;
			Estado_desv_i :  in std_logic;
			Estado_ante_o :  out std_logic;
			Estado_post_o :  out std_logic;
			Estado_desv_o :  out std_logic;
			Cambio_i :  in std_logic;
			Cambio_o :  out std_logic
		);
	end entity cambio_11;
architecture Behavioral of cambio_11 is
begin
	process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			Cambio_o <= Cambio_i;
			if (Cambio_i = '0') then
				Estado_ante_o <= Estado_post_i;
				Estado_post_o <= Estado_ante_i;
				Estado_desv_o <= '0';
			else
				Estado_ante_o <= Estado_desv_i;
				Estado_post_o <= '0';
				Estado_desv_o <= Estado_ante_i;
			end if;
		end if;
	end process;
end Behavioral;