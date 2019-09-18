library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity sum2op is
	generic(
		N: natural := 4
	);
	port(
		a_i: in std_logic_vector(N-1 downto 0);
		b_i: in std_logic_vector(N-1 downto 0);
		s_o: out std_logic_vector(N-1 downto 0)

	);
end;

architecture sum2op_arq of sum2op is
begin
	s_o <= std_logic_vector(unsigned(a_i) + unsigned(b_i));
end;