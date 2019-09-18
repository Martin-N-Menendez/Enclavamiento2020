library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity sum_top is
	generic(
		N: natural := 4;
		SEL: natural := 0
	);
	port(
		a_i: in std_logic_vector(N-1 downto 0);
		b_i: in std_logic_vector(N-1 downto 0);
		c_i: in std_logic_vector(N-1 downto 0);
		s_o: out std_logic_vector(N-1 downto 0)

	);
end;

architecture sum_top_arq of sum_top is
begin

	gen_0: if SEL = 0 generate
			sum2op_gen: entity work.sum2op
				generic map(
					N => N
				)
				port map(
					a_i => a_i,
					b_i => b_i,
					s_o => s_o
				);
		end generate;
		
	gen_1: if SEL = 1 generate
			sum2op_gen: entity work.sum3op
				generic map(
					N => N
				)
				port map(
					a_i => a_i,
					b_i => b_i,
					c_i => c_i,
					s_o => s_o
				);
		end generate;

end;