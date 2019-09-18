library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity componente_top is
	port(
		a_i: in std_logic_vector(3 downto 0);
		b_i: in std_logic_vector(3 downto 0);
		s_o: out std_logic_vector(3 downto 0)

	);
end;

architecture componente_top_arq of componente_top is
begin

	inst: entity work.sum_top
		generic map(
			N => 4,
			SEL => 1	-- 0: sumador de 2 operandos
						-- 1: sumador de 3 operandos
		)
		port map(
			a_i => a_i,
			b_i => b_i,
			c_i => "1011",
			s_o => s_o
		);

end;