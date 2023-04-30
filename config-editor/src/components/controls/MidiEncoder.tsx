import { Circle, Select, Text, VStack } from "@chakra-ui/react";

export default function Encoder(props: { encoderNum: number; layer: string }) {
  let eNum = props.encoderNum;
  // if (props.layer === "B") {
  //   eNum = props.encoderNum + 8;
  // }
  return (
    <VStack>
      <Circle size="16" bg="teal">
        <Text>E{eNum}</Text>
      </Circle>
      <Select placeholder="Turn Action" size={"xs"}>
        <option value="option1">Pan</option>
        <option value="option2">Tilt</option>
        <option value="option3">Option 3</option>
      </Select>
      <Select placeholder="Press Action" size={"xs"}>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
      </Select>
    </VStack>
  );
}
