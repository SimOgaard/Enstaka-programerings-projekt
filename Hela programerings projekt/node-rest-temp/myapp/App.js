import React from 'react';

import {
  createStackNavigator,
} from 'react-navigation';

import Screen1 from './app/components/screen1/Screen1';

const StackNavigator = createStackNavigator({
    Screen1: { 
        screen: Screen1,
        navigationOptions: {
            title: false,
            header: null,
        }
    },
},{ headerMode: 'screen' });

export default class App extends React.Component {
    render() {
        return (
            <StackNavigator/>
        );
    }
};